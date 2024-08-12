from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from db.func import create_user
from shared.decorators import handler_exception
from .text import start_message


router = Router()

@router.message(CommandStart())
@handler_exception
async def command_start_handler(message: Message) -> None:
    await create_user(
        user_id=message.from_user.id,
        username=message.from_user.username
    )
    await message.answer(
        start_message["message"]
    )