from typing import List
from datetime import datetime

import pytz
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert

from config.user_settings import TIMEZONE
from .session import async_session_maker
from .models import User, DEFAULT_FIRST_NAME, DEFAULT_LAST_NAME, DEFAULT_USERNAME, DEFAULT_LANGUAGE


async def update_last_action(tg_userid: int) -> None:
    async with async_session_maker() as session:
        await session.execute(
            update(User)
            .where(User.tg_userid == tg_userid)
            .values(last_action=datetime.now(pytz.timezone(TIMEZONE)))
        )
        await session.commit()


async def get_all_users() -> List[User]:
    async with async_session_maker() as session:
        result = await session.execute(select(User))
        return result.scalars().all()


async def exist_user(tg_userid: int) -> bool:
    async with async_session_maker() as session:
        result = await session.execute(select(User).filter(User.tg_userid == tg_userid))
        return result.scalar() is not None


async def register_user(
    tg_userid: int,
    username: str = DEFAULT_USERNAME,
    first_name: str = DEFAULT_FIRST_NAME,
    last_name: str = DEFAULT_LAST_NAME,
    language: str = DEFAULT_LANGUAGE
) -> None:
    async with async_session_maker() as session:
        stmt = insert(User).values(
            tg_userid=tg_userid,
            username=username or DEFAULT_USERNAME,
            first_name=first_name or DEFAULT_FIRST_NAME,
            last_name=last_name or DEFAULT_LAST_NAME,
            language=language or DEFAULT_LANGUAGE,
        ).on_conflict_do_nothing(index_elements=['tg_userid'])
        await session.execute(stmt)
        await session.commit()


async def get_user_lang(tg_userid: int) -> str:
    async with async_session_maker() as session:
        result = await session.execute(select(User.language).filter(User.tg_userid == tg_userid))
        return result.scalar() or DEFAULT_LANGUAGE


async def update_user_lang(tg_userid: int, language: str) -> None:
    async with async_session_maker() as session:
        await session.execute(
            update(User)
            .where(User.tg_userid == tg_userid)
            .values(language=language)
        )
        await session.commit()
