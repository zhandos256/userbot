from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config.const import SQLITE_DB_URL, DEBUG

engine = create_async_engine(url=SQLITE_DB_URL, echo=True if DEBUG else False)
async_session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False,)
