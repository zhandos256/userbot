import signal
import asyncio
import logging
from typing import Tuple, Optional

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramAPIError

from config.routers import main_router
from config.user_settings import settings, POLLING_TIMEOUT
from config.logger import setup_logging
from database.session import async_session_maker
from middlewares.i18n_middleware import i18n_middleware
from middlewares.last_action_middleware import LastActionMiddleware
from utils.notify import notify_admins
from utils.commands import get_bot_commands


async def notify_startup(bot: Bot) -> None:
    """Уведомляет админов о запуске бота и настраивает команды."""
    try:
        await bot.set_my_commands(commands=get_bot_commands())
        await bot.delete_webhook(drop_pending_updates=True)
        await notify_admins(bot=bot, text="Бот запущен!")
    except TelegramAPIError as e:
        logging.error(f"Ошибка Telegram API при запуске бота: {e}")
    except Exception as e:
        logging.error(f"Неожиданная ошибка при запуске бота: {e}")


async def notify_shutdown(bot: Bot) -> None:
    """Уведомляет админов об остановке бота."""
    try:
        await notify_admins(bot=bot, text="Бот остановлен!")
    except TelegramAPIError as e:
        logging.error(f"Ошибка Telegram API при остановке бота: {e}")
    except Exception as e:
        logging.error(f"Неожиданная ошибка при остановке бота: {e}")


async def initialize_bot_and_dispatcher() -> Tuple[Bot, Dispatcher]:
    """Инициализирует бота и диспетчер, регистрирует middleware и роутеры."""
    bot = Bot(
        token=settings.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()
    # Register routers
    dp.include_router(main_router)
    # Register handlers
    dp.startup.register(notify_startup)
    dp.shutdown.register(notify_shutdown)
    # Register middlwares
    dp.update.middleware.register(LastActionMiddleware(async_session_maker))
    dp.update.middleware.register(i18n_middleware)
    return bot, dp


async def run_bot() -> None:
    """Run bot and handle exceptions"""
    bot: Optional[Bot] = None
    dp: Optional[Dispatcher] = None
    try:
        bot, dp = await initialize_bot_and_dispatcher()
        await dp.start_polling(bot, polling_timeout=POLLING_TIMEOUT)
    except TelegramAPIError as e:
        logging.error(f"Ошибка Telegram API при работе бота: {e}")
    except Exception as e:
        logging.exception(f"Неожиданная ошибка при работе бота: {e}")
    finally:
        if dp:
            await dp.storage.close()
        if bot:
            await bot.session.close()


def main() -> None:
    """Main execute bot command"""
    setup_logging()
    loop = asyncio.get_event_loop()
    try:
        # Register signals
        loop.add_signal_handler(signal.SIGINT, lambda: loop.stop())
        loop.add_signal_handler(signal.SIGTERM, lambda: loop.stop())
        # Run bots
        loop.run_until_complete(run_bot())
    except KeyboardInterrupt:
        logging.info("Бот остановлен пользователем.")
    finally:
        loop.close()


if __name__ == "__main__":
    main()
