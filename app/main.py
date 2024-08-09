import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import command_handler
from menu import setup_bot_commands


TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


async def main() -> None:
    bot = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp.startup.register(setup_bot_commands)
    dp.include_routers(
        command_handler.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())