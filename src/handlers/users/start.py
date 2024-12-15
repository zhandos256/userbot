from aiogram import Router, types
from aiogram.filters import Command

from db.query import register_user
from keyboards.inline.menu import menu_kb

router = Router()


@router.message(Command("start"))
async def start_msg_handler(msg: types.Message):
    await register_user(
        userid=msg.from_user.id,
        username=msg.from_user.username,
        first_name=msg.from_user.first_name,
        last_name=msg.from_user.last_name,
    )
    template_msg = [
        "Шаблонное приветствие\n",
        "Поменяй меня на другой текст\n",
        "Исходники - https://github.com/zhandos256/templateaiogram\n",
    ]
    await msg.answer(text="\n".join(template_msg), reply_markup=await menu_kb())
