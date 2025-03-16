from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from keyboards.inline.menu import back_menu_kb

router = Router()

ECHO_MSG = (
    "Извините, я не смог понять ваше сообщение. Используйте команду /help, чтобы увидеть доступные команды.",
)


@router.message()
async def echo_handler(msg: types.Message, state: FSMContext):
    st = await state.get_state()
    if st is None:
        await msg.answer(text="\n".join(ECHO_MSG), reply_markup=back_menu_kb())
