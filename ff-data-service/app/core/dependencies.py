# app/core/dependencies.py
from app.core.config import settings, Settings
from app.core.db import SessionLocal


def get_settings() -> Settings:
    return settings

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()