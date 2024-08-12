from aiogram import Router
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

from aiogram.filters.command import Command
from aiogram.types import Message

from shared.decorators import handler_exception
from .service import service_get_stastitics
from .text import (
    about_text, 
    full_access_text, 
    demo_access_text, 
    tg_id_text,
    what_next_text,
    stastitics_text
)
from .service import (
    service_demo_access_key,
    service_full_access_key,
)


router = Router()

@router.message(Command(about_text["key"]))
@handler_exception
async def command_about_handler(message: Message) -> None:
    await message.answer(
        about_text["message"], 
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=what_next_text["value"],
                        callback_data=what_next_text["key"]
                    )
                ]
            ]
        )
    )


@router.message(Command(tg_id_text["key"]))
@handler_exception
async def command_tg_id_handler(message: Message) -> None:
    await message.answer(
        tg_id_text["message"].format(
            username=message.from_user.username, 
            id=message.from_user.id
        )
    )


@router.message(Command(full_access_text["key"]))
@handler_exception
async def command_full_access_handler(message: Message) -> None:
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
                            text=demo_access_text["value"],
                            callback_data=demo_access_text["callback"]
                        )
                    ]
                ]
            )
        )


@router.message(Command(demo_access_text["key"]))
@handler_exception
async def command_demo_access_handler(message: Message) -> None:
    message_text = await service_demo_access_key(
        user_id=message.from_user.id, 
        username=message.from_user.username,
    )
    await message.answer(message_text)


@router.message(Command(stastitics_text["key"]))
@handler_exception
async def command_get_stastitics(message: Message) -> None:
    message_text = await service_get_stastitics(
        user_id=message.from_user.id
    )
    await message.answer(message_text)