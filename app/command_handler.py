from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message

from commands import commands
from func_outline import OutlineManager, OneGigabyte, bytes_to_gb


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message(Command(commands["access_key"]["key"]))
async def command_get_access_key(message: Message) -> None:
    user_id = message.from_user.id
    manager = OutlineManager()
    user_data = await manager.get_key(user_id)
    if user_data == OutlineManager.not_foud:
        user_data = await manager.create_key(
            user_id,
            name=message.from_user.username,
            limit={"bytes": OneGigabyte.value},
        )
    message_text = commands["access_key"]["message"].format(
        limit=OneGigabyte.name, 
        key=user_data["accessUrl"]
    )
    await message.answer(message_text, parse_mode="MarkdownV2")


@router.message(Command(commands["stastitics"]["key"]))
async def command_get_stastitics(message: Message) -> None:
    manager = OutlineManager()
    user_id = message.from_user.id
    transferred_data = await manager.get_transferred_data_per_user(user_id)
    user_data = await manager.get_key(user_id)
    if data_limit := user_data.get("dataLimit", None):
        message_text = commands["stastitics"]["message"].format(
            transferred_data=transferred_data,
            limit=bytes_to_gb(data_limit["bytes"])
        )
    else:
        message_text = commands["stastitics"]["message_without_limit"].format(
            transferred_data=transferred_data
        )
    await message.answer(message_text)
