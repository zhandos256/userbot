from typing import Union

from aiogram import types
from aiogram.filters import BaseFilter

from database.queries import get_all_users


class IsAdmin(BaseFilter):
    async def __call__(self, obj: Union[types.Message, types.CallbackQuery]) -> bool:
        return obj.from_user.id in [user.tg_userid for user in await get_all_users() if user.is_admin]

