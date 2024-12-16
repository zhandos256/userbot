import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

from core.const import BOT_TOKEN, DEBUG, LOG_FILE
from handlers.admin import admin
from handlers.users import about, cancel, echo, help, lang, menu, settings, start
from middleware.I18nMiddleware import i18n_middleware
from misc.bot_commands import set_bot_commands
from misc.notify import notify_admins


async def on_startup(bot: Bot):
    await notify_admins(bot=bot, text="Бот запущен!")


async def on_shutdown(bot: Bot):
    await notify_admins(bot=bot, text="Бот остановлен!")


async def configure():
    bot = Bot(token=BOT_TOKEN if BOT_TOKEN else "define me!", parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        start.router,
        help.router,
        menu.router,
        settings.router,
        about.router,
        lang.router,
        admin.router,
        cancel.router,
        echo.router,
    )
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware.register(i18n_middleware)
    await set_bot_commands(bot=bot)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.exception(e)
    finally:
        await dp.storage.close()
        await bot.session.close()


def main():
    logging.basicConfig(
        filename=LOG_FILE,
        filemode='a',
        level=logging.INFO if not DEBUG else logging.DEBUG
    )
    asyncio.run(configure())
