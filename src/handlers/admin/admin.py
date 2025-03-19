from aiogram import Router, types
from aiogram.filters import Command

from filters.admin import IsAdmin

router = Router()


@router.message(IsAdmin(), Command("admin"))
async def admin_msg_handler(msg: types.Message):
    await msg.answer(text="Админ панель")
