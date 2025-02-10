from aiogram import F, Router, types
from aiogram.filters import Command

from keyboards.inline.menu import back_menu_kb

router = Router()

tmp_msg = (
    "Шаблонное приветствие\n",
    "Исходники - https://github.com/zhandos256/templateaiogram\n",
)


@router.message(Command("help"))
async def help_msg(msg: types.Message):
    await msg.answer(text="\n".join(tmp_msg), reply_markup=back_menu_kb())


@router.callback_query(F.data == "help_callback_data")
async def help_cb(call: types.CallbackQuery):
    await call.message.edit_text(
        text="\n".join(tmp_msg), reply_markup=back_menu_kb()
    )
