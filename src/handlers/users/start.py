from aiogram import Router, types
from aiogram.filters import CommandStart

from database.query import get_user_repository
from keyboards.inline.lang import start_lang_kb
from keyboards.inline.menu import menu_kb

router = Router()


@router.message(CommandStart())
async def start_msg_handler(msg: types.Message):
    user_repo = await get_user_repository()
    user = await user_repo.exist_user(tg_userid=msg.from_user.id)
    if not user:
        await msg.answer(text='Выберите язык интерфейса', reply_markup=start_lang_kb())
    else:
        template_msg = [
            "Шаблонное приветствие\n",
            "Исходники - https://github.com/zhandos256/templateaiogram\n",
        ]
        await msg.answer(text="\n".join(template_msg), reply_markup=menu_kb())
