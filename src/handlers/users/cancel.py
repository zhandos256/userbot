from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from keyboards.inline.menu import back_menu_kb

router = Router()


@router.message(Command("cancel"))
async def cancel_msg(msg: types.Message, state: FSMContext):
    st = await state.get_state()
    if st is not None:
        await msg.answer(
            text="Операция отменена!", reply_markup=await back_menu_kb()
        )
        await state.clear()
    else:
        await msg.answer(text="Нечего отменять!", reply_markup=await back_menu_kb())


@router.callback_query(F.data == "cancel")
async def cancel_cb(call: types.CallbackQuery, state: FSMContext):
    st = await state.get_state()
    if st is not None:
        await call.message.edit_text(
            text="Операция отменена!", reply_markup=await back_menu_kb()
        )
        await state.clear()
    else:
        await call.answer(text="Нечего отменять!", show_alert=True)
