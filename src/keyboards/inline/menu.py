from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Настройки", callback_data="settings"))
    builder.add(InlineKeyboardButton(text="О боте", callback_data="about"))
    return builder.as_markup()


def back_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Меню", callback_data="menu"))
    return builder.as_markup()
