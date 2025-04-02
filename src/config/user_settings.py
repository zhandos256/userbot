from enum import Enum
from typing import Final
from pathlib import Path
from datetime import datetime

import pytz
from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings

# Main paths
BASE_DIR: Final[Path] = Path(__file__).parent.parent
LOGS_DIR: Final[Path] = BASE_DIR / "logs"
LOCALES_DIR: Final[Path] = BASE_DIR / "locales"
SQLITE_DB_FILE: Final[Path] = BASE_DIR / "db.sqlite"

# Const
TIMEZONE: Final[str] = "Asia/Almaty"
POLLING_TIMEOUT: Final[int] = 5
DEFAULT_SQLITE_URL: Final[str] = f"sqlite+aiosqlite:///{SQLITE_DB_FILE}"
DEFAULT_POSTGRES_URL: Final[str] = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"


class DBType(str, Enum):
    SQLITE = "sqlite"
    POSTGRES = "postgres"


def generate_log_file(logs_dir: Path = LOGS_DIR) -> Path:
    """Generate log file path based on current date."""
    tz = pytz.timezone(TIMEZONE)
    date_str = datetime.now(tz).strftime("%Y-%m-%d")
    return logs_dir / f"{date_str}.log"


class Settings(BaseSettings):
    # Режим отладки
    debug: bool = True

    # Конфиденциальные настройки
    bot_token: SecretStr = Field(..., env="BOT_TOKEN")
    postgres_db_url: SecretStr = Field(default=DEFAULT_POSTGRES_URL, env="POSTGRES_DB_URL")

    # Настройки базы данных
    db_type: DBType = Field(default=DBType.SQLITE, env="DB_TYPE")

    # Локализация
    domain_messages: str = "messages"
    default_locale: str = "ru"

    # Логирование
    log_file: Path = Field(default_factory=generate_log_file)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False  # Добавлено для гибкости


# Инициализация настроек
settings = Settings()

# Создание директории логов (выполняется один раз при импорте)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Словарь URL баз данных
DB_URLS: Final[dict[DBType, str]] = {
    DBType.SQLITE: DEFAULT_SQLITE_URL,
    DBType.POSTGRES: settings.postgres_db_url.get_secret_value(),
}

# URL текущей базы данных
DATABASE_URL: Final[str] = DB_URLS[settings.db_type]