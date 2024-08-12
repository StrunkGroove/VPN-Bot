from aiogram import Router
from aiogram.types import Message
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.filters.command import Command

from shared.decorators import handler_exception
from shared.service import is_admin
from .text import statistics_text, set_user_vip_text, update_text


router = Router()


@router.message(Command(update_text["key"]))
@handler_exception
async def command_admin_update(message: Message) -> None:
    if await is_admin(user_id=message.from_user.id):
        return await message.answer(
            update_text["message"], 
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(
                            text=set_user_vip_text["value"],
                            callback_data=set_user_vip_text["callback"]
                        ),
                        InlineKeyboardButton(
                            text=statistics_text["value"],
                            callback_data=statistics_text["callback"]
                        ),
                    ]
                ]
            )
        )
    await message.answer(
        update_text["on_exceptions"]
    )