from enum import Enum
from pathlib import Path
from datetime import datetime

import pytz
from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings


class DBType(str, Enum):
    SQLITE = "sqlite"
    POSTGRES = "postgres"


def generate_log_file() -> Path:
    """
    Генерирует путь к лог-файлу на основе текущей даты.

    Returns:
        Path: Путь к файлу логов
    """
    date_str = datetime.now(pytz.timezone(settings.TIMEZONE)).strftime("%Y-%m-%d")
    return settings.LOGS_DIR / f"{date_str}.log"


class Settings(BaseSettings):
    # Основные настройки
    DEBUG: bool = True
    TIMEZONE: str = "Asia/Almaty"
    BOT_TOKEN: SecretStr = Field(..., env="BOT_TOKEN")
    POLLING_TIMEOUT: int = 5

    # Пути к директориям
    BASE_DIR: Path = Path(__file__).parent.parent
    LOGS_DIR: Path = BASE_DIR / "logs"
    LOCALES_DIR: Path = BASE_DIR / "locales"

    # Настройки базы данных
    DB_TYPE: DBType = Field(default=DBType.SQLITE, env="DB_TYPE")
    SQLITE_DB_FILE_PATH: Path = BASE_DIR / "db.sqlite"
    SQLITE_DB_URL: str = f"sqlite+aiosqlite:///{SQLITE_DB_FILE_PATH}"
    POSTGRES_DB_URL: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres",
        env="POSTGRES_DB_URL"
    )

    # Настройки локализации
    DOMAIN_MESSAGES: str = "messages"
    DEFAULT_LOCALE: str = "ru"

    # Путь к файлу логов
    LOG_FILE: Path = Field(default_factory=generate_log_file)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)

DB_URLS = {
    DBType.SQLITE: settings.SQLITE_DB_URL,
    DBType.POSTGRES: settings.POSTGRES_DB_URL,
}

DATABASE_URL = DB_URLS.get(settings.DB_TYPE, settings.SQLITE_DB_URL)