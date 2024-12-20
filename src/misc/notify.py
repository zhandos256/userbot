import asyncio
import logging

from aiogram import Bot

from db.query import get_all_users


async def notify_admins(bot: Bot, text: str):
    users = await get_all_users()
    if users is not None:
        for user in users:
            if user.is_admin:
                try:
                    await bot.send_message(chat_id=user.tg_userid, text=text)
                    await asyncio.sleep(0.05)
                except Exception as e:
                    logging.exception(e)


async def notify_users(bot: Bot, text: str):
    users = await get_all_users()
    if users is not None:
        for user in users:
            if not user.is_admin:
                try:
                    await bot.send_message(chat_id=user.tg_userid, text=text)
                    await asyncio.sleep(0.05)
                except Exception as e:
                    logging.exception(e)
