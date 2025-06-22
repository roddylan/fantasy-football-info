# app/core/dependencies.py
from app.core.config import settings, Settings

def get_settings() -> Settings:
    return settings

