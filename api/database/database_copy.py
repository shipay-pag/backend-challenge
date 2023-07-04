import api.helpers.env
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api.database.models import User, Role, Claim, UserClaim

Base = declarative_base()

# engine = create_engine('postgresql://postgres:postgres@localhost:5432/shipay')
engine = create_engine(os.getenv('DATABASE_URL'))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Questão 2 ----------------------------------------------------------------------------------------------------------------------------
query = session.query(User.name, User.email, Role.description.label('role_description'), Claim.description.label('claim_description')) \
    .join(Role, User.role_id == Role.id) \
    .join(UserClaim, User.id == UserClaim.user_id) \
    .join(Claim, Claim.id == UserClaim.claim_id)

results = query.all()

for result in results:
    name, email, role_description, claim_description = result
    print(f"Name: {name}, Email: {email}, Role Description: {role_description}, Claim Description: {claim_description}")
