from typing import Optional

from sqlalchemy import select

from db.config import async_session_maker
from db.models import User


async def get_all_users():
    async with async_session_maker() as session:
        query = select(User)
        resutl = await session.execute(query)
        return resutl.scalars().all()


async def exist_user(tg_userid: int):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=tg_userid)
        result = await session.execute(query)
        return True if result else False


async def register_user(
    userid: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    language: str = "ru"
):
    async with async_session_maker() as session:
        # Check user if existing
        query = select(User).filter_by(tg_userid=userid)
        result = await session.execute(query)
        exist_user = result.scalar_one_or_none()
        if exist_user:
            return

        new_user = User(
            tg_userid=userid,
            username=username if username else "-",
            first_name=first_name if first_name else "-",
            last_name=last_name if last_name else "-",
            language=language
        )
        session.add(new_user)
        await session.commit()


async def get_user_lang(userid: int):
    async with async_session_maker() as session:
        query = select(User.language).filter_by(tg_userid=userid)
        result = await session.execute(query)
        language = result.scalar_one_or_none()
        return language


async def update_user_lang(userid: int, value: str):
    async with async_session_maker() as session:
        query = select(User).filter_by(tg_userid=userid)
        result = await session.execute(query)
        user = result.scalar_one_or_none()
        user.language = value
        await session.commit()
