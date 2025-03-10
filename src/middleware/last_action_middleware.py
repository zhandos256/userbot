from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker

from database.query import update_last_action


class LastActionMiddleware(BaseMiddleware):
    def __init__(self, async_sessoin: async_sessionmaker):
        self.async_sessoin = async_sessoin
        super().__init__()

    async def __call__(self, handler, event, data):
        # return await super().__call__(handler, event, data)
        user = data["event_from_user"]
        user_id = int(user.id)
        await update_last_action(tg_userid=user_id)
        return await handler(event, data)