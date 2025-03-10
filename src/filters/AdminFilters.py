from typing import Union

from aiogram import types
from aiogram.filters import BaseFilter

from database.query import get_user_repository


class IsAdmin(BaseFilter):
    async def __call__(self, obj: Union[types.Message, types.CallbackQuery]) -> bool:
        if obj.from_user:
            user_id = obj.from_user.id
            user_repo = await get_user_repository()
            users = await user_repo.get_all_users()
            return user_id in [user.tg_userid for user in users if user.is_admin]
