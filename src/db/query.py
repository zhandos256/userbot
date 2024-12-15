from sqlalchemy import select

from db.config import async_session_maker, engine
from db.models import Base, User


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_all_users():
    async with async_session_maker() as session:
        query = select(User)
        resutl = await session.execute(query)
        return resutl.scalars().all()


async def register_user(
    userid: int, username: str = None, first_name: str = None, last_name: str = None
):
    async with async_session_maker() as session:
        # Check user if existing
        query = select(User).filter_by(userid=userid)
        result = await session.execute(query)
        exist_user = result.scalar_one_or_none()
        if exist_user:
            return

        new_user = User(
            userid=userid,
            username=username if username else "-",
            first_name=first_name if first_name else "-",
            last_name=last_name if last_name else "-",
        )
        session.add(new_user)
        await session.commit()


async def get_user_lang(userid: int):
    async with async_session_maker() as session:
        query = select(User).filter_by(userid=userid)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        if not user:
            return
        return user.language


async def update_user_lang(userid: int, value: str):
    async with async_session_maker() as session:
        query = select(User).filter_by(userid=userid)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        if not user:
            return
        user.language = value
        await session.commit()
