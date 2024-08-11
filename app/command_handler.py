from aiogram import Router
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.types import Message

from decorators import exception_handler
from db import create_user
from text import (
    menu_commands, 
    start_message, 
    additional_commands, 
    admin_commands
)
from service import (
    service_demo_access_key,
    service_get_stastitics,
    service_full_access_key,
    is_admin
)


router = Router()


@router.message(CommandStart())
@exception_handler
async def command_start_handler(message: Message) -> None:
    await create_user(
        user_id=message.from_user.id,
        username=message.from_user.username
    )
    await message.answer(
        start_message["message"]
    )


@router.message(Command(menu_commands["about"]["key"]))
@exception_handler
async def command_about_handler(message: Message) -> None:
    await message.answer(
        menu_commands["about"]["message"], 
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=additional_commands["what_next"]["value"],
                        callback_data=additional_commands["what_next"]["key"]
                    )
                ]
            ]
        )
    )


@router.message(Command(menu_commands["get_tg_id"]["key"]))
@exception_handler
async def command_get_tg_id(message: Message) -> None:
    await message.answer(
        menu_commands["get_tg_id"]["message"].format(
            username=message.from_user.username, 
            id=message.from_user.id
        )
    )


@router.message(Command(menu_commands["full_access_key"]["key"]))
@exception_handler
async def command_get_full_access_key(message: Message) -> None:
    status, message_text = await service_full_access_key(
        user_id=message.from_user.id, 
        username=message.from_user.username,
    )
    if status:
        await message.answer(message_text)
    elif not status:
        await message.answer(
            message_text,
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=menu_commands["demo_access_key"]["value"],
                            callback_data=menu_commands["demo_access_key"]["callback"]
                        )
                    ]
                ]
            )
        )


@router.message(Command(menu_commands["demo_access_key"]["key"]))
@exception_handler
async def command_get_demo_access_key(message: Message) -> None:
    message_text = await service_demo_access_key(
        user_id=message.from_user.id, 
        username=message.from_user.username,
    )
    await message.answer(message_text)


@router.message(Command(menu_commands["stastitics"]["key"]))
@exception_handler
async def command_get_stastitics(message: Message) -> None:
    message_text = await service_get_stastitics(
        user_id=message.from_user.id
    )
    await message.answer(message_text)


@router.message(Command(admin_commands["update"]["key"]))
@exception_handler
async def command_admin_update(message: Message) -> None:
    if await is_admin(user_id=message.from_user.id):
        return await message.answer(
            admin_commands["update"]["message"], 
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=admin_commands["set_user_vip"]["value"],
                            callback_data=admin_commands["set_user_vip"]["callback"]
                        ),
                        InlineKeyboardButton(
                            text=admin_commands["statistics"]["value"],
                            callback_data=admin_commands["statistics"]["callback"]
                        ),
                    ]
                ]
            )
        )
    await message.answer(
        admin_commands["update"]["on_exceptions"]
    )