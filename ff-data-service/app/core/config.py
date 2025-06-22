# app/core/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_user: str
    db_password: str