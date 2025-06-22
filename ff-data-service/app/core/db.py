# app/core/db.py

from app.core.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models.base import Base

db_url = settings.db_url


engine = create_engine(db_url)

SessionLocal = sessionmaker(engine)

def init_db():
    Base.metadata.create_all(engine)