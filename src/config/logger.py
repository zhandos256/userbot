import sys
import logging

from config.user_settings import settings, LOGS_DIR


# Константы для логирования
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_LEVEL = logging.DEBUG if settings.debug else logging.INFO


def setup_logging() -> None:
    """Настраивает логгирование в зависимости от режима DEBUG.
    
    В режиме DEBUG логи выводятся в stdout.
    В продакшн режиме логи записываются в файл.
    """
    # Создаем директорию для логов, если она не существует
    if not settings.debug:
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Базовые параметры для логгера
    common_params = {
        "level": LOG_LEVEL,
        "format": LOG_FORMAT,
        "datefmt": DATE_FORMAT,
    }
    
    # Настройка вывода логов
    if settings.debug:
        common_params["stream"] = sys.stdout
    else:
        common_params["filename"] = settings.log_file
        common_params["filemode"] = "a"
    
    # Настройка логгера
    logging.basicConfig(**common_params)
    
    # Логируем информацию о настройке
    logging.info(
        f"Логгер настроен: {'DEBUG' if settings.debug else 'INFO'} уровень, "
        f"{'stdout' if settings.debug else f'файл {settings.log_file}'}"
    ) 