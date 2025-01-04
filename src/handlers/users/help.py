from aiogram import F, Router, types
from aiogram.filters import Command

from keyboards.inline.menu import back_menu_kb

router = Router()


@router.message(Command("help"))
async def help_msg(msg: types.Message):
    template_msg = [
        "Шаблонное приветствие\n",
        "Поменяй меня на другой текст\n",
        "Исходники - https://github.com/zhandos256/templateaiogram\n",
    ]
    await msg.answer(text="\n".join(template_msg), reply_markup=back_menu_kb())


@router.callback_query(F.data == "help_callback_data")
async def help_cb(call: types.CallbackQuery):
    template_msg = [
        "Помощь\n",
        "/start - Старт бота",
        "/help - Получить помощь",
        "/start - Меню",
    ]
    await call.message.edit_text(
        text="\n".join(template_msg), reply_markup=back_menu_kb()
    )
