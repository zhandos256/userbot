from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    BOT_COMMANDS = [
        BotCommand(command="/start", description="Template start message"),
        BotCommand(command="/help", description="Template help message"),
        BotCommand(command="/menu", description="Template menu message"),
    ]
    await bot.set_my_commands(BOT_COMMANDS)