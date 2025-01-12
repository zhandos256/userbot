from datetime import datetime
from os import getenv
from pathlib import Path

from aiogram.types import BotCommand

DEBUG = 0

BOT_TOKEN = getenv("BOT_TOKEN", "DEFINE ME!")

BASE_DIR = Path(__file__).parent.parent
LOGS_DIR = BASE_DIR / 'logs'
LOG_FILE = LOGS_DIR / f"{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.log"
DB_URL = getenv("DB_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres")
LOCALES_DIR = BASE_DIR / "locales"

BOT_COMMANDS = [
    BotCommand(command="/start", description="Template start message"),
    BotCommand(command="/help", description="Template help message"),
    BotCommand(command="/menu", description="Template menu message"),
]
