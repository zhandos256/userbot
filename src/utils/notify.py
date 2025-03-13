import asyncio
import logging

from aiogram import Bot

from database.query import get_all_users


async def notify_users_by_condition(bot: Bot, text: str, is_admin: bool):
    users = await get_all_users()
    if users is not None:
        for user in users:
            if user.is_admin == is_admin:
                try:
                    await bot.send_message(chat_id=user.tg_userid, text=text)
                    await asyncio.sleep(0.05)
                except Exception as e:
                    logging.exception(e)


async def notify_admins(bot: Bot, text: str):
    await notify_users_by_condition(bot, text, is_admin=True)


async def notify_users(bot: Bot, text: str):
    await notify_users_by_condition(bot, text, is_admin=False)
