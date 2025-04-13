import textwrap

from aiogram import Router, types
from aiogram.filters import CommandStart

from database.user_queries import exist_user
from keyboards.inline.menu import menu_kb
from keyboards.inline.lang import start_lang_kb

router = Router()


@router.message(CommandStart())
async def start_handler(msg: types.Message):
    user = await exist_user(tg_userid=msg.from_user.id)
    if not user:
        await msg.answer(text='Выберите язык интерфейса', reply_markup=start_lang_kb())
    else:
        start_msg = textwrap.dedent(
            """
            Шаблонное приветствие

            Исходники - https://github.com/zhandos256/templateaiogram
            """
        )
        await msg.answer(text=start_msg, reply_markup=menu_kb())
