from typing import Union 

from aiogram import F, Router, types
from aiogram.filters import Command

from keyboards.inline.menu import menu_kb

router = Router()

MENU_MSG = (
    "Шаблонное приветствие\n",
    "Исходники - https://github.com/zhandos256/templateaiogram\n",
)


async def msg_handler(upd: types.Message) -> None:
    await upd.answer(text="\n".join(MENU_MSG), reply_markup=menu_kb())


async def callback_handler(upd: types.CallbackQuery) -> None:
    await upd.message.edit_text(text="\n".join(MENU_MSG), reply_markup=menu_kb())


handlers = {
    types.Message: msg_handler,
    types.CallbackQuery: callback_handler,
}


@router.message(Command("menu"))
@router.callback_query(F.data == "menu")
async def menu_handler(update: Union[types.Message, types.CallbackQuery]) -> None:
    handler = handlers.get(type(update))
    if handler is None:
        return
    await handler(update)