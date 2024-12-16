from datetime import datetime
from os import getenv
from pathlib import Path

from aiogram.types import BotCommand

DEBUG = 0

BOT_TOKEN = getenv("BOT_TOKEN")

BASE_DIR = Path(__file__).parent.parent
LOGS_DIR = BASE_DIR / 'logs'
LOG_FILE = LOGS_DIR / f"{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.log"
DB_FILE_PATH = BASE_DIR / "db.sqlite"
DB_URL = f"sqlite+aiosqlite:///{DB_FILE_PATH}"
LOCALES_DIR = BASE_DIR / "locales"

BOT_COMMANDS = [
    BotCommand(command="/start", description="Template start message"),
    BotCommand(command="/help", description="Template help message"),
    BotCommand(command="/menu", description="Template menu message"),
]
