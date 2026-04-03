''''
This module sets up the database connection and defines the base class for the ORM models.
connects to SQLite -> creates a database session -> defines a base class for models
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///data/weather.db"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()