import api.helpers.env
import os
from faker import Faker
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from random import randint, choice
from api.database.models import User, Role, Claim, UserClaim

DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASS = os.environ.get('DATABASE_PASS')

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()


def get_random_role_id():
    role = session.query(Role).order_by(func.random()).first()
    return role.id


def generate_users(num_users):
    users = []
    for _ in range(num_users):
        user = User(
            name=faker.name(),
            email=faker.email(),
            password=faker.password(),
            created_at=datetime.now(),
            updated_at=datetime.now(),
            role_id=get_random_role_id()
        )
        users.append(user)
    session.add_all(users)
    session.commit()


def generate_roles():
    roles = [
        Role(description='Administrador'),
        Role(description='Moderador'),
        Role(description='Usuário'),
        Role(description='TI')
    ]
    session.add_all(roles)
    session.commit()


def generate_claims(num_claims):
    claims = []
    for _ in range(num_claims):
        claim = Claim(
            description=faker.word(),
            active=faker.boolean()
        )
        claims.append(claim)
    session.add_all(claims)
    session.commit()


def assign_user_claims():
    users = session.query(User).all()
    claims = session.query(Claim).all()
    for user in users:
        num_claims = randint(1, len(claims))
        user_claims = user.claims  # Claims já existentes para o usuário

        # IDs das Claims existentes
        # Utilizando Set's para chaves únicas
        existing_claim_ids = {uc.claim_id for uc in user_claims}

        for _ in range(num_claims):
            claim = choice(claims)
            if claim.id not in existing_claim_ids:
                user_claim = UserClaim(user=user, claim=claim)
                session.add(user_claim)
                existing_claim_ids.add(claim.id)

    session.commit()


# Gerar dados dinamicamente para as tabelas
generate_roles()
generate_users(10)
generate_claims(5)
assign_user_claims()

print("Banco de dados populado com sucesso!")
