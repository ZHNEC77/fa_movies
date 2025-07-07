import logging
from pathlib import Path

from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class DbConfig(BaseModel):
    path: Path = BASE_DIR / "db_sqlite3"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)
    db: DbConfig = DbConfig()
    run: RunConfig = RunConfig()


settings = Settings()
