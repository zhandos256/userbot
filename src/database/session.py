from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config.const import DATABASE_URL, settings

engine = create_async_engine(url=DATABASE_URL, echo=True if settings.DEBUG else False)
async_session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False,)
