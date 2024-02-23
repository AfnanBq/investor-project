from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""This file is to create the base model for the database. It also creates the session for the database."""

SQLALCHEMY_DATABASE_URL = (
    "cockroachdb://root@localhost:26257/investor_bulletin?sslmode=disable"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False,autoflush = False,bind = engine)

Base = declarative_base()
