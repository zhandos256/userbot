from datetime import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from config.const import TIMEZONE
from .models import User
from .session import async_session_maker


class UserRepository():
    def __init__(self, session: AsyncSession):
        self.session = session

    async def update_last_action(self, tg_userid: int):
        result = await self.session.execute(select(User).filter(User.tg_userid == tg_userid))
        user = result.scalar_one_or_none()
        if user:
            user.last_action = datetime.now(TIMEZONE)
            await self.session.commit()


    async def get_all_users(self):
        result = await self.session.execute(select(User))
        return result.scalars().all()


    async def exist_user(self, tg_userid: int):
        user = await self.session.execute(select(User).filter(User.tg_userid == tg_userid))
        return user.scalar_one_or_none() is not None


    async def register_user(
        self,
        tg_userid: int,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        language: str = "ru"
    ):
        # Check user if existing
        result = await self.session.execute(select(User).filter(User.tg_userid == tg_userid))
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
        self.session.add(new_user)
        await self.session.commit()


    async def get_user_lang(self, tg_userid: int):
        result = await self.session.execute(select(User.language).filter(User.tg_userid == tg_userid))
        return result.scalar_one_or_none()


    async def update_user_lang(self, tg_userid: int, value: str):
        result = await self.session.execute(select(User).filter(User.tg_userid == tg_userid))
        user = result.scalar_one_or_none()
        if user:
            user.language = value
            await self.session.commit()


async def get_user_repository():
    async with async_session_maker() as session:
        return UserRepository(session=session)