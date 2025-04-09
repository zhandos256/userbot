from aiogram import BaseMiddleware
from aiogram.types import User as AiogramUser
from sqlalchemy.ext.asyncio import async_sessionmaker

from database.user_queries import update_last_action


class LastActionMiddleware(BaseMiddleware):
    def __init__(self, async_sessoin: async_sessionmaker):
        self.async_sessoin = async_sessoin
        super().__init__()

    async def __call__(self, handler, event, data):
        user: AiogramUser = data["event_from_user"]
        await update_last_action(tg_userid=user.id)
        return await handler(event, data)