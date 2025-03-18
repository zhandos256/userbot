from pydantic import Field
from pydantic_settings import BaseSettings
from pathlib import Path
from datetime import datetime
from enum import Enum
import pytz

class DBType(str, Enum):
    SQLITE = "sqlite"
    POSTGRES = "postgres"

class Settings(BaseSettings):
    DEBUG: bool = False
    TIMEZONE: str = "Asia/Almaty"
    BOT_TOKEN: str = Field(..., env="BOT_TOKEN")
    BASE_DIR: Path = Path(__file__).parent.parent
    LOGS_DIR: Path = BASE_DIR / "logs"
    SQLITE_DB_FILE_PATH: Path = BASE_DIR / "db.sqlite"
    SQLITE_DB_URL: str = f"sqlite+aiosqlite:///{SQLITE_DB_FILE_PATH}"
    POSTGRES_DB_URL: str = Field(default="postgresql+asyncpg://postgres:postgres@localhost:5432/postgres", env="POSTGRES_DB_URL")
    DB_TYPE: DBType = Field(default=DBType.SQLITE, env="DB_TYPE")
    LOCALES_DIR: Path = BASE_DIR / "locales"
    DOMAIN_MESSAGES: str = "messages"
    DEFAULT_LOCALE: str = "ru"
    POLLING_TIMEOUT: int = 5
    LOG_FILE: Path = LOGS_DIR / f"{datetime.now(pytz.timezone((TIMEZONE))).strftime('%Y-%m-%d')}.log"


settings = Settings()
# Создание директории для логов
settings.LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Настройка URL базы данных
DB_URLS = {
    DBType.SQLITE: settings.SQLITE_DB_URL,
    DBType.POSTGRES: settings.POSTGRES_DB_URL,
}

DATABASE_URL = DB_URLS.get(settings.DB_TYPE, settings.SQLITE_DB_URL)

# Команды бота
from aiogram.types import BotCommand

def get_bot_commands() -> list[BotCommand]:
    return [
        BotCommand(command="/start", description="Template start message"),
        BotCommand(command="/help", description="Template help message"),
        BotCommand(command="/menu", description="Template menu message"),
    ]

COMMANDS = get_bot_commands()