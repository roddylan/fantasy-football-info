# app/core/db.py

from app.core.config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = settings.db_url


engine = create_engine(db_url)

SessionLocal = sessionmaker(engine)

