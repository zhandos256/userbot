from typing import Union

from aiogram import types
from aiogram.filters import BaseFilter

from db.query import get_all_users


class IsAdmin(BaseFilter):
    async def __call__(self, obj: Union[types.Message, types.CallbackQuery]) -> bool:
        users = await get_all_users()
        if users is None:
            return False
        user_id = obj.from_user.id
        return user_id in [user.userid for user in users if user.is_admin]
