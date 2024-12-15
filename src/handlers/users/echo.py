from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from keyboards.inline.menu import back_menu_kb

router = Router()


@router.message()
async def echo_msg(msg: types.Message, state: FSMContext):
    st = await state.get_state()
    if st is not None:
        pass
    else:
        template_msg = [
            "Извините, я не смог понять ваше сообщение. Используйте команду /help, чтобы увидеть доступные команды.",
        ]
        await msg.answer(text="\n".join(template_msg), reply_markup=await back_menu_kb())
