from aiogram import Router, types
from aiogram.filters import CommandStart

from database.queries import exist_user
from keyboards.inline.lang import start_lang_kb
from keyboards.inline.menu import menu_kb

router = Router()


@router.message(CommandStart())
async def start_handler(msg: types.Message):
    user = await exist_user(tg_userid=msg.from_user.id)
    if not user:
        await msg.answer(text='Выберите язык интерфейса', reply_markup=start_lang_kb())
    else:
        start_msg = [
            "Шаблонное приветствие\n",
            "Исходники - https://github.com/zhandos256/templateaiogram\n",
        ]
        await msg.answer(text="\n".join(start_msg), reply_markup=menu_kb())
