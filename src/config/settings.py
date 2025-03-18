import asyncio
import logging
import signal
import sys
from typing import Tuple

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config.routers import main_router
from config.const import settings, COMMANDS
from database.queries import async_session_maker
from middleware.i18n_middleware import i18n_middleware
from middleware.last_action_middleware import LastActionMiddleware
from utils.notify import notify_admins


async def notify_startup(bot: Bot) -> None:
    """Уведомляет админов о запуске бота и настраивает команды."""
    try:
        await bot.set_my_commands(commands=COMMANDS)
        await bot.delete_webhook(drop_pending_updates=True)
        await notify_admins(bot=bot, text="Бот запущен!")
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")


async def notify_shutdown(bot: Bot) -> None:
    """Уведомляет админов об остановке бота."""
    try:
        await notify_admins(bot=bot, text="Бот остановлен!")
    except Exception as e:
        logging.error(f"Ошибка при остановке бота: {e}")


async def initialize_bot_and_dispatcher() -> Tuple[Bot, Dispatcher]:
    """Инициализирует бота и диспетчер, регистрирует middleware и роутеры."""
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(main_router)
    dp.startup.register(notify_startup)
    dp.shutdown.register(notify_shutdown)
    dp.update.middleware.register(LastActionMiddleware(async_session_maker))
    dp.update.middleware.register(i18n_middleware)
    return bot, dp


async def run_bot() -> None:
    """Запускает бота и обрабатывает исключения."""
    bot, dp = await initialize_bot_and_dispatcher()
    try:
        await dp.start_polling(bot, polling_timeout=settings.POLLING_TIMEOUT)
    except Exception as e:
        logging.exception(f"Ошибка при работе бота: {e}")
    finally:
        await dp.storage.close()
        await bot.session.close()


def setup_logging() -> None:
    """Настраивает логгирование в зависимости от режима DEBUG."""
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    datefmt = "%Y-%m-%d %H:%M:%S"
    common_params = {
        "level": logging.DEBUG if settings.DEBUG else logging.INFO,
        "format": log_format,
        "datefmt": datefmt,
    }
    if settings.DEBUG:
        common_params["stream"] = sys.stdout
    else:
        common_params["filename"] = settings.LOG_FILE
        common_params["filemode"] = "a"
    logging.basicConfig(**common_params)


def main() -> None:
    """Основная функция для запуска бота."""
    setup_logging()
    loop = asyncio.get_event_loop()
    try:
        loop.add_signal_handler(signal.SIGINT, lambda: loop.stop())
        loop.add_signal_handler(signal.SIGTERM, lambda: loop.stop())
        loop.run_until_complete(run_bot())
    except KeyboardInterrupt:
        logging.info("Бот остановлен пользователем.")
    finally:
        loop.close()


if __name__ == "__main__":
    main()