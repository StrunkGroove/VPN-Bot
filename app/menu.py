from aiogram import Bot
from aiogram.types.bot_command import BotCommand

from commands import commands


async def setup_bot_commands(bot: Bot):
    bot_commands = [
        BotCommand(command=command["key"], description=command["value"])
        for command in commands.values()
    ]
    await bot.set_my_commands(bot_commands)