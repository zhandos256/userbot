from typing import List
from datetime import datetime

import pytz
from sqlalchemy import select, update
from sqlalchemy.dialects.postgresql import insert

from config.user_settings import settings
from .models import User, DEFAULT_FIRST_NAME, DEFAULT_LAST_NAME, DEFAULT_USERNAME, DEFAULT_LANGUAGE, DEFAULT_IS_ADMIN
from .session import async_session_maker


async def update_last_action(tg_userid: int) -> None:
    """
    Обновляет время последнего действия пользователя в базе данных.

    Args:
        tg_userid (int): Telegram ID пользователя
    """
    async with async_session_maker() as session:
        await session.execute(
            update(User)
            .where(User.tg_userid == tg_userid)
            .values(last_action=datetime.now(pytz.timezone(settings.TIMEZONE)))
        )
        await session.commit()


async def get_all_users() -> List[User]:
    """
    Получает список всех пользователей из базы данных.

    Returns:
        List[User]: Список объектов пользователей
    """
    async with async_session_maker() as session:
        result = await session.execute(select(User))
        return result.scalars().all()


async def exist_user(tg_userid: int) -> bool:
    """
    Проверяет существование пользователя в базе данных.

    Args:
        tg_userid (int): Telegram ID пользователя

    Returns:
        bool: True если пользователь существует, False в противном случае
    """
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
    """
    Регистрирует нового пользователя в базе данных.

    Args:
        tg_userid (int): Telegram ID пользователя
        username (Optional[str]): Имя пользователя в Telegram
        first_name (Optional[str]): Имя пользователя
        last_name (Optional[str]): Фамилия пользователя
        language (str): Код языка пользователя (по умолчанию "ru")
    """
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
    """
    Получает язык пользователя из базы данных.

    Args:
        tg_userid (int): Telegram ID пользователя

    Returns:
        str: Код языка пользователя (по умолчанию "ru")
    """
    async with async_session_maker() as session:
        result = await session.execute(select(User.language).filter(User.tg_userid == tg_userid))
        return result.scalar() or DEFAULT_LANGUAGE


async def update_user_lang(tg_userid: int, language: str) -> None:
    """
    Обновляет язык пользователя в базе данных.

    Args:
        tg_userid (int): Telegram ID пользователя
        language (str): Новый код языка пользователя
    """
    async with async_session_maker() as session:
        await session.execute(
            update(User)
            .where(User.tg_userid == tg_userid)
            .values(language=language)
        )
        await session.commit()
