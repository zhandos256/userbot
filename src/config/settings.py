import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

from config.routers import main_router
from config.const import  BOT_TOKEN, DEBUG, LOG_FILE, COMMANDS
from database.queries import async_session_maker
from middleware.i18n_middleware import i18n_middleware
from middleware.last_action_middleware import LastActionMiddleware
from utils.notify import notify_admins


async def on_startup(bot: Bot):
    await bot.set_my_commands(commands=COMMANDS)
    await bot.delete_webhook(drop_pending_updates=True)
    await notify_admins(bot=bot, text="Бот запущен!")


async def on_shutdown(bot: Bot):
    await notify_admins(bot=bot, text="Бот остановлен!")


async def configure_bot():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(main_router)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware.register(LastActionMiddleware(async_session_maker))
    dp.update.middleware.register(i18n_middleware)
    try:
        await dp.start_polling(bot, polling_timeout=5)
    except Exception as e:
        logging.exception(e)
    finally:
        await dp.storage.close()
        await bot.session.close()


def configure_logger():
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    common_params = {
        "level": logging.INFO,
        "format": log_format,
        "datefmt": datefmt,
    }
    if DEBUG:
        common_params["stream"] = sys.stdout
    else:
        common_params["filename"] = LOG_FILE
        common_params["filemode"] = "a"
    logging.basicConfig(**common_params)


def main():
    configure_logger()
    asyncio.run(configure_bot())
