from functools import lru_cache
from typing import List

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    secret_token: str = Field(..., env='SECRET_TOKEN')
    allow_origins: List[str] = Field(..., env='ALLOW_ORIGINS')

    class Config:
        env_file = '.env'


@lru_cache
def get_settings():
    return Settings()
