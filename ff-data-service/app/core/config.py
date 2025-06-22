# app/core/config.py

from pydantic_settings import BaseSettings
from app.core.utils import is_running_in_docker
if not is_running_in_docker():
    try:
        from dotenv import load_dotenv # temporary

        load_dotenv()
    except ImportError:
        print("Failed to import")

class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    
    
    @property
    def db_url(self):
        return f'postgresql://{self.db_user}:{self.db_password}@{self.db_host}/football_info'
settings = Settings()