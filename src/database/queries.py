from datetime import datetime
from typing import Optional

from sqlalchemy import select

from config.const import TIMEZONE
from .models import User
from .session import async_session_maker


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
        return user.scalar_one_or_none() is not None


async def register_user(
    tg_userid: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    language: str = "ru"
):
    async with async_session_maker() as session:
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


async def update_user_lang(tg_userid: int, language: str):
    async with async_session_maker() as session:
        result = await session.execute(select(User).filter(User.tg_userid == tg_userid))
        user = result.scalar_one_or_none()
        if user:
            user.language = language
            await session.commit()