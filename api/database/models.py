from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class User(Base):
    """
    Classe que define a tabela 'users' do banco de dados.

    Atributos:
        id (Column): Coluna para o ID do usuário (chave primária).
        name (Column): Coluna para o nome do usuário.
        email (Column): Coluna para o e-mail do usuário (único).
        password (Column): Coluna para a senha do usuário.
        created_at (Column): Coluna para a data de criação do usuário.
        updated_at (Column): Coluna para a data de atualização do usuário.
        role_id (Column): Coluna para a referência à tabela 'roles' (chave estrangeira).

        role (relationship): Relacionamento com a tabela 'roles'.
        claims (relationship): Relacionamento com a tabela 'user_claims'.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    role_id = Column(Integer, ForeignKey('roles.id'))

    role = relationship("Role", back_populates="users")
    claims = relationship("UserClaim", back_populates="user")


class Role(Base):
    """
    Classe que define a tabela 'roles' do banco de dados.

    Atributos:
        id (Column): Coluna para o ID da função (chave primária).
        description (Column): Coluna para a descrição da função.

        users (relationship): Relacionamento com a tabela 'users'.
    """
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    description = Column(String)

    users = relationship("User", back_populates="role")


class UserClaim(Base):
    """
    Classe que define a tabela de associação 'user_claims' do banco de dados.

    Atributos:
        user_id (Column): Coluna para a referência ao ID do usuário (chave primária).
        claim_id (Column): Coluna para a referência ao ID da reivindicação (chave primária).

        user (relationship): Relacionamento com a tabela 'users'.
        claim (relationship): Relacionamento com a tabela 'claims'.
    """
    __tablename__ = 'user_claims'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    claim_id = Column(Integer, ForeignKey('claims.id'), primary_key=True)

    user = relationship("User", back_populates="claims")
    claim = relationship("Claim")


class Claim(Base):
    """
    Classe que define a tabela 'claims' do banco de dados.

    Atributos:
        id (Column): Coluna para o ID da reivindicação (chave primária).
        description (Column): Coluna para a descrição da reivindicação.
        active (Column): Coluna para indicar se a reivindicação está ativa ou não.
    """
    __tablename__ = 'claims'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    active = Column(Boolean)
