from aiogram import Bot
from aiogram.types.bot_command import BotCommand

from text import menu_commands


async def setup_bot_commands(bot: Bot):
    bot_commands = [
        BotCommand(command=command["key"], description=command["value"])
        for command in menu_commands.values()
    ]
    await bot.set_my_commands(bot_commands)