from aiogram import F, Router, types

from keyboards.inline.menu import back_menu_kb

router = Router()


@router.callback_query(F.data == "about")
async def about(call: types.CallbackQuery):
    template_msg = (
        "О боте\n",
        "Исходники - https://github.com/zhandos256/templateaiogram\n",
    )
    await call.message.edit_text(text="\n".join(template_msg), reply_markup=back_menu_kb())
