from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def settings_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Язык интерфейса", callback_data="lang"))
    builder.add(InlineKeyboardButton(text="Меню", callback_data="menu"))
    return builder.as_markup()
