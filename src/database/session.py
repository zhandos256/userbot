from sqlalchemy.pool import AsyncAdaptedQueuePool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config.user_settings import DATABASE_URL, settings


# Константы для конфигурации пула соединений
POOL_SIZE = 5
MAX_OVERFLOW = 10
POOL_TIMEOUT = 30
POOL_RECYCLE = 1800  # 30 минут


def create_engine() -> create_async_engine:
    """Создает асинхронный движок SQLAlchemy с настроенным пулом соединений.
    
    Returns:
        create_async_engine: Настроенный асинхронный движок SQLAlchemy
    """
    return create_async_engine(
        url=DATABASE_URL,
        echo=settings.debug,
        poolclass=AsyncAdaptedQueuePool,
        pool_size=POOL_SIZE,
        max_overflow=MAX_OVERFLOW,
        pool_timeout=POOL_TIMEOUT,
        pool_recycle=POOL_RECYCLE,
    )


# Создаем движок и фабрику сессий
engine = create_engine()
async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
