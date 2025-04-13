import textwrap

from aiogram import F, Router, types

from keyboards.inline.menu import back_menu_kb

router = Router()

ABOUT_MSG = textwrap.dedent(
    """
    О боте

    Исходники - https://github.com/zhandos256/templateaiogram
    """
)


@router.callback_query(F.data == "about")
async def about_handler(call: types.CallbackQuery):
    await call.message.edit_text(text=ABOUT_MSG, reply_markup=back_menu_kb())
