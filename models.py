from sqlalchemy import Column, Date, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL
Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)

    users = relationship('User', back_populates='role') 

class Claim(Base):
    __tablename__ = 'claims'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, default=True)

    users = relationship('User', secondary='user_claims', back_populates='claims')



class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date)

    role = relationship('Role', back_populates='users')
    claims = relationship('Claim', secondary='user_claims', back_populates='users')


class UserClaim(Base):
    __tablename__ = 'user_claims'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    claim_id = Column(Integer, ForeignKey('claims.id'), primary_key=True)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


