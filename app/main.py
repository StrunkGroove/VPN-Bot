import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import command_handler
import message_handler
import callbacks
from menu import setup_bot_commands
from db import initialize_indexes


TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher(storage=MemoryStorage())


async def main() -> None:
    bot = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp.startup.register(setup_bot_commands)
    dp.startup.register(initialize_indexes)
    dp.include_routers(
        command_handler.router,
        message_handler.router,
        callbacks.router
    )
    await dp.start_polling(bot, skip_updates=False)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, 
        stream=sys.stdout
    )
    asyncio.run(main())