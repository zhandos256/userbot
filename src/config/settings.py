import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

from config.const import  BOT_TOKEN, DEBUG, LOG_FILE
from database.queries import async_session_maker
from handlers.admin.admin import router as admin_router
from handlers.users.start import router as start_router
from handlers.users.help import router as help_router
from handlers.users.about import router as about_router
from handlers.users.lang import router as lang_router
from handlers.users.cancel import router as cancel_router
from handlers.users.echo import router as echo_router
from handlers.users.menu import router as menu_router
from handlers.users.settings import router as settings_router
from middleware.i18n_middleware import i18n_middleware
from middleware.last_action_middleware import LastActionMiddleware
from utils import bot_commands, notify


async def on_startup(bot: Bot):
    await bot.delete_webhook(drop_pending_updates=True)
    await bot_commands.set_bot_commands(bot=Bot)
    await notify.notify_admins(bot=bot, text="Бот запущен!")


async def on_shutdown(bot: Bot):
    await notify.notify_admins(bot=bot, text="Бот остановлен!")


async def configure_bot():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        cancel_router, start_router, help_router, menu_router,
        about_router, settings_router, lang_router, admin_router,
        echo_router,
    )
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
