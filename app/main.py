import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from menu.main import router as menu_router
from menu.setup import setup_commands
from admin.main import router as main_router
from start.main import router as start_router
from db.schemas import initialize_indexes


TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher(storage=MemoryStorage())


async def main() -> None:
    bot = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp.startup.register(setup_commands)
    dp.startup.register(initialize_indexes)
    dp.include_routers(
        menu_router,
        main_router,
        start_router
    )
    await dp.start_polling(bot, skip_updates=False)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, 
        stream=sys.stdout
    )
    asyncio.run(main())