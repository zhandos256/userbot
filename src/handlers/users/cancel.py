from typing import Union

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.inline.menu import back_menu_kb

router = Router()


async def msg_with_state(upd: types.Message) -> None:
    await upd.answer(text="Операция отменена!", reply_markup=back_menu_kb())


async def msg_without_state(upd: types.Message) -> None:
    await upd.answer(text="Нечего отменять!", reply_markup=back_menu_kb())


async def callback_with_state(upd: types.CallbackQuery) -> None:
    await upd.message.edit_text(text="Операция отменена!", reply_markup=back_menu_kb())


async def callback_without_state(upd: types.CallbackQuery) -> None:
    await upd.answer(text="Нечего отменять!", show_alert=True)


@router.message(Command("cancel"))
@router.callback_query(F.data == "cancel")
async def cancel_msg(update: Union[types.Message, types.CallbackQuery], state: FSMContext) -> None:
    st = await state.get_state()

    handlers = {
        types.Message: {
            "with_state": msg_with_state,
            "without_state": msg_without_state,
        },
        types.CallbackQuery: {
            "with_state": callback_with_state,
            "without_state": callback_without_state,
        }
    }

    handler = handlers.get(type(update))
    if handler is None:
        return

    if st is not None:
        await handler["with_state"](update)
        await state.clear()
    else:
        await handler["without_state"](update)
