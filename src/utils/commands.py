from aiogram.types import BotCommand


def get_bot_commands() -> list[BotCommand]:
    return [
        BotCommand(command="/start", description="Template start message"),
        BotCommand(command="/help", description="Template help message"),
        BotCommand(command="/menu", description="Template menu message"),
    ] 