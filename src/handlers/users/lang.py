from aiogram import F, Router, types

from db.query import update_user_lang, register_user
from keyboards.inline.lang import lang_kb
from keyboards.inline.menu import back_menu_kb, menu_kb

router = Router()


@router.callback_query(F.data == "lang")
async def lang_cb(call: types.CallbackQuery):
    await call.message.edit_text(
        text="Язык интерфейса", reply_markup=lang_kb())


@router.callback_query(F.data == 'kk')
async def update_lang_kk(call: types.CallbackQuery):
    await update_user_lang(userid=call.from_user.id, value="kk")
    await call.message.edit_text(
        text="Интерфейс тілі жаңартылды!", reply_markup=back_menu_kb()
    )


@router.callback_query(F.data == 'ru')
async def update_lang_ru(call: types.CallbackQuery):
    await update_user_lang(userid=call.from_user.id, value="ru")
    await call.message.edit_text(
        text="Язык интерфейса обновлен!", reply_markup=back_menu_kb()
    )


@router.callback_query(F.data == 'kk_start')
async def update_lang_kk_start(call: types.CallbackQuery):
    await register_user(
        userid=call.from_user.id,
        username=call.from_user.username,
        first_name=call.from_user.first_name,
        last_name=call.from_user.last_name,
        language="kk"
    )
    template_msg = [
        "Шаблонное приветствие\n",
        "Поменяй меня на другой текст\n",
        "Исходники - https://github.com/zhandos256/templateaiogram\n",
    ]
    await call.message.edit_text(
        text="\n".join(template_msg), reply_markup=menu_kb()
    )


@router.callback_query(F.data == 'ru_start')
async def update_lang_ru_start(call: types.CallbackQuery):
    await register_user(
        userid=call.from_user.id,
        username=call.from_user.username,
        first_name=call.from_user.first_name,
        last_name=call.from_user.last_name,
        language="kk"
    )
    template_msg = [
        "Шаблонное приветствие\n",
        "Поменяй меня на другой текст\n",
        "Исходники - https://github.com/zhandos256/templateaiogram\n",
    ]
    await call.message.edit_text(
        text="\n".join(template_msg), reply_markup=menu_kb()
    )
