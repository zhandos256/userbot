from aiogram import F, Router, types

from database.user_queries import register_user, update_user_lang
from keyboards.inline.lang import lang_kb
from keyboards.inline.menu import back_menu_kb, menu_kb

router = Router()

lang_messages = {
    'kk': 'Интерфейс тілі жаңартылды!',
    'ru': 'Язык интерфейса обновлен!'
}


@router.callback_query(F.data == "lang")
async def lang_cb(call: types.CallbackQuery):
    await call.message.edit_text(text="Язык интерфейса", reply_markup=lang_kb())


@router.callback_query(F.data.in_(['kk', 'ru']))
async def update_lang(call: types.CallbackQuery):
    await update_user_lang(tg_userid=call.from_user.id, language=call.data)
    await call.message.edit_text(text=lang_messages[call.data], reply_markup=back_menu_kb())


@router.callback_query(F.data.in_(["kk_start", "ru_start"]))
async def update_lang_start(call: types.CallbackQuery):
    lang = "kk" if call.data == "kk_start" else "ru"
    await register_user(
        tg_userid=call.from_user.id,
        username=call.from_user.username,
        first_name=call.from_user.first_name,
        last_name=call.from_user.last_name,
        language=lang
    )
    temp_msg = (
        "Шаблонное приветствие\n",
        "Исходники - https://github.com/zhandos256/templateaiogram\n",
    )
    await call.message.edit_text(text="\n".join(temp_msg), reply_markup=menu_kb())
