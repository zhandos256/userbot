from os import getenv
from pathlib import Path
from datetime import datetime

import pytz

DEBUG = 0

TIMEZONE = pytz.timezone("Asia/Almaty")

BOT_TOKEN = getenv("BOT_TOKEN", "define me!")

BASE_DIR = Path(__file__).parent.parent

LOGS_DIR = BASE_DIR / 'logs'
LOG_FILE = LOGS_DIR / f"{datetime.now(TIMEZONE).strftime('%Y-%m-%d')}.log"

SQLITE_DB_FILE_PATH = BASE_DIR / "db.sqlite"
SQLITE_DB_URL = f"sqlite+aiosqlite:///{SQLITE_DB_FILE_PATH}"

# If you want use Postgres
# replace SQLITE_DB_URL to this and in env.py
# POSTGRES_DB_URL = getenv(
#     "POSTGRES_DB_URL",
#     "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
# )

LOCALES_DIR = BASE_DIR / "locales"
DOMAIN_MESSAGES = "messages"
DEFAULT_LOCALE = 'ru'

from aiogram.types import BotCommand
COMMANDS = [
    BotCommand(command="/start", description="Template start message"),
    BotCommand(command="/help", description="Template help message"),
    BotCommand(command="/menu", description="Template menu message"),
]