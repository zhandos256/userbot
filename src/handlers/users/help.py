from typing import Union

from aiogram.filters import Command
from aiogram import F, Router, types

from keyboards.inline.menu import back_menu_kb

router = Router()

HELP_MSG = (
    "Шаблонное приветствие\n",
    "Исходники - https://github.com/zhandos256/templateaiogram\n",
)


async def callback_handler(update: types.CallbackQuery) -> None:
    await update.message.edit_text(text="\n".join(HELP_MSG), reply_markup=back_menu_kb())


async def msg_handler(update: types.Message) -> None:
    await update.answer(text="\n".join(HELP_MSG), reply_markup=back_menu_kb())


handlers = {
    types.CallbackQuery: callback_handler,
    types.Message: msg_handler,
}


@router.message(Command("help"))
@router.callback_query(F.data == "help_callback_data")
async def help_handler(update: Union[types.Message, types.CallbackQuery]) -> None:
    handler = handlers.get(type(update))
    if handler is None:
        return
    await handler(update)
