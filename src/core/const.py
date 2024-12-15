from os import getenv
from pathlib import Path

DEBUG = 0

BOT_TOKEN = getenv("BOT_TOKEN")

BASE_DIR = Path(__file__).parent.parent
DB_FILE_PATH = BASE_DIR / "db.sqlite"
DB_URL = f"sqlite+aiosqlite:///{DB_FILE_PATH}"
LOCALES_DIR = BASE_DIR / "locales"
