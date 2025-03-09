from datetime import datetime
from typing import Optional

from sqlalchemy import select

from db.config import async_session_maker
from core.const import TIMEZONE
from db.models import User


async def update_last_action(tg_userid: int):
    async with async_session_maker() as session:
        result = await session.execute(select(User).filter(User.tg_userid == tg_userid))
        user = result.scalar_one_or_none()
        if user:
            user.last_action = datetime.now(TIMEZONE)
            await session.commit()


async def get_all_users():
    async with async_session_maker() as session:
        result = await session.execute(select(User))
        return result.scalars().all()


async def exist_user(tg_userid: int):
    async with async_session_maker() as session:
        user = await session.execute(select(User).filter(User.tg_userid == tg_userid))
        return True if user.scalar_one_or_none() else False


async def register_user(
    tg_userid: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    language: str = "ru"
):
    async with async_session_maker() as session:
        # Check user if existing
        result = await session.execute(select(User).filter(User.tg_userid == tg_userid))
        exist_user = result.scalar_one_or_none()
        if exist_user:
            return
        new_user = User(
            tg_userid=tg_userid,
            username=username if username else "-",
            first_name=first_name if first_name else "-",
            last_name=last_name if last_name else "-",
            language=language
        )
        session.add(new_user)
        await session.commit()


async def get_user_lang(tg_userid: int):
    async with async_session_maker() as session:
        result = await session.execute(select(User.language).filter(User.tg_userid == tg_userid))
        return result.scalar_one_or_none()


async def update_user_lang(tg_userid: int, value: str):
    async with async_session_maker() as session:
        result = await session.execute(select(User).filter(User.tg_userid == tg_userid))
        user = result.scalar_one_or_none()
        if user:
            user.language = value
            await session.commit()
