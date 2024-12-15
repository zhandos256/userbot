from aiogram import Router, types
from aiogram.filters import Command

from filters.AdminFilters import IsAdmin

router = Router()


@router.message(IsAdmin(), Command("admin"))
async def admin_msg_handler(msg: types.Message):
    template_msg = [
        "Админ панель\n",
    ]
    await msg.answer(text="\n".join(template_msg), reply_markup=None)
