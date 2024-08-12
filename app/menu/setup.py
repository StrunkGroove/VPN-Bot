from aiogram import Bot
from aiogram.types.bot_command import BotCommand

from .text import (
    about_text, 
    full_access_text, 
    demo_access_text, 
    stastitics_text, 
    tg_id_text
)


async def setup_commands(bot: Bot):
    bot_commands = [
        BotCommand(
            command=about_text["key"], 
            description=about_text["value"]
        ),
        BotCommand(
            command=full_access_text["key"], 
            description=full_access_text["value"]
        ),
        BotCommand(
            command=demo_access_text["key"], 
            description=demo_access_text["value"]
        ),
        BotCommand(
            command=stastitics_text["key"], 
            description=stastitics_text["value"]
        ),
        BotCommand(
            command=tg_id_text["key"], 
            description=tg_id_text["value"]
        )
    ]
    await bot.set_my_commands(bot_commands)