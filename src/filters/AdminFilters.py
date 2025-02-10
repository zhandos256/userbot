from typing import Union

from aiogram import types
from aiogram.filters import BaseFilter

from db.query import get_all_users

class IsAdmin(BaseFilter):
    async def __call__(self, obj: Union[types.Message, types.CallbackQuery]) -> bool:
        user_id = obj.from_user.id
        users = await get_all_users()
        return user_id in [user.tg_userid for user in users if user.is_admin]
