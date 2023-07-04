import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASS = os.environ.get('DATABASE_PASS')

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}/{DATABASE_NAME}"

Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base.metadata.create_all(engine)