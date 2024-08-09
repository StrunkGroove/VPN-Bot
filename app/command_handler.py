from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message

from commands import commands
from func_outline import OutlineManager


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message(Command(commands["access_key"]["key"]))
async def command_get_access_key(message: Message) -> None:
    manager = OutlineManager()
    response = await manager.get_keys()
    await message.answer("Хер тебе ! Пока что)")


@router.message(Command(commands["stastitics"]["key"]))
async def command_get_stastitics(message: Message) -> None:
    await message.answer(f"Hello, get_stastitics!")
