# app/core/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_user: str
    db_password: str
    
    
    @property
    def db_url(self):
        return f'postgres://{self.db_user}:{self.db_password}@db/football_info'
settings = Settings()