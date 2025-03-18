from datetime import datetime
from typing import Optional

import pytz
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert

from config.const import settings
from .models import User
from .session import async_session_maker


async def update_last_action(tg_userid: int):
    async with async_session_maker() as session:
        await session.execute(
            update(User)
            .where(User.tg_userid == tg_userid)
            .values(last_action=datetime.now(pytz.timezone(settings.TIMEZONE)))
        )
        await session.commit()


async def get_all_users():
    async with async_session_maker() as session:
        result = await session.execute(select(User))
        return result.scalars().all()


async def exist_user(tg_userid: int):
    async with async_session_maker() as session:
        result = await session.execute(select(User).filter(User.tg_userid == tg_userid))
        return result.scalar() is not None


async def register_user(
    tg_userid: int,
    username: Optional[str] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    language: str = "ru"
):
    async with async_session_maker() as session:
        stmt = insert(User).values(
            tg_userid=tg_userid,
            username=username or "-",
            first_name=first_name or "-",
            last_name=last_name or "-",
            language=language
        ).on_conflict_do_nothing(index_elements=['tg_userid'])
        await session.execute(stmt)
        await session.commit()
            

async def get_user_lang(tg_userid: int):
    async with async_session_maker() as session:
        result = await session.execute(select(User.language).filter(User.tg_userid == tg_userid))
        return result.scalar() or "ru"


async def update_user_lang(tg_userid: int, language: str):
    async with async_session_maker() as session:
        await session.execute(
            update(User)
            .where(User.tg_userid == tg_userid)
            .values(language=language)
        )
        await session.commit()