from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
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
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    description = Column(String)

    users = relationship("User", back_populates="role")


class UserClaim(Base):
    __tablename__ = 'user_claims'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    claim_id = Column(Integer, ForeignKey('claims.id'), primary_key=True)

    user = relationship("User", back_populates="claims")
    claim = relationship("Claim")


class Claim(Base):
    __tablename__ = 'claims'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    active = Column(Boolean)