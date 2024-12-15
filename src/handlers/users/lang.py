from aiogram import F, Router, types

from db.query import update_user_lang
from keyboards.inline.lang import lang_kb
from keyboards.inline.menu import back_menu_kb

router = Router()


@router.callback_query(F.data == "lang")
async def lang_cb(call: types.CallbackQuery):
    await call.message.edit_text(text="Язык интерфейса", reply_markup=await lang_kb())


@router.callback_query(F.data.in_(["kk", "ru"]))
async def menu_cb_handler(call: types.CallbackQuery):
    if F.data == "kk":
        await update_user_lang(userid=call.from_user.id, value="kk")
    else:
        await update_user_lang(userid=call.from_user.id, value="ru")
    await call.message.edit_text(
        text="Язык интерфейса обновлен!", reply_markup=await back_menu_kb()
    )
