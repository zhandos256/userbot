from aiogram import  Router, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command

from filters.AdminFilters import IsAdminMsg


router = Router()


@router.message(IsAdminMsg(), Command('admin'))
async def admin_msg_handler(msg: types.Message):
    template = [
        'Админ панель\n',
    ]
    await msg.answer(
        text='\n'.join(template),
        reply_markup=None,
        parse_mode=ParseMode.HTML
    )
