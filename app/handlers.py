import logging

from aiogram import Router, html
from aiogram.enums.chat_member_status import ChatMemberStatus
from aiogram.filters import Command, CommandStart
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup
from decouple import config

from api.x_ui_api import X_UI_API
from app.decorators import catch_errors
from app.utlis import get_vpn_link

router = Router()
logger = logging.getLogger("vpn_bot")


@router.message(CommandStart())
@catch_errors
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="/help")]],
        resize_keyboard=True,
        one_time_keyboard=False,
    )

    text = (
        f"👋 Привет, <b>{message.from_user.full_name}</b>!\n\n"
        "Чтобы получить VPN ссылку, введите команду:\n"
        "/vpn"
    )
    await message.answer(text, parse_mode="HTML", reply_markup=keyboard)


@router.message(Command("help"))
@catch_errors
async def command_help_handler(message: Message) -> None:
    help_text = (
        "👋 Привет!\n\n"
        "Чтобы получить свою VPN ссылку, просто введи команду:\n"
        "🔑 /vpn\n\n"
        "По вопросам обращайться: @StrunkGroove"
    )
    await message.answer(help_text)


@router.message(Command("vpn"))
@catch_errors
async def command_vpn_handler(message: Message) -> None:
    member = await message.bot.get_chat_member(
        chat_id=config("CHANNEL_ID"), user_id=message.from_user.id
    )
    if member.status not in [
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.CREATOR,
    ]:
        return await message.answer(
            "🚫 Так как вы не подписаны на канал, то не можете получить VPN ссылку.\n"
            "Обратитесь к администратору: @StrunkGroove"
        )

    vpn_link = get_vpn_link(message.from_user.id)
    if not vpn_link:
        email = (
            message.from_user.username
            if message.from_user.username
            else message.from_user.id
        )
        X_UI_API.add_client_to_inbound(tg_id=message.from_user.id, email=email)
        vpn_link = get_vpn_link(message.from_user.id)

    message_text = (
        f"<pre><code>{vpn_link}</code></pre>\n"
        "🔗 Пожалуйста, скопируйте ссылку и вставьте в приложение."
    )

    await message.answer(message_text, parse_mode="HTML")


@router.message()
@catch_errors
async def on_any_message(message: Message) -> None:
    await message.answer("❓ Если нужна помощь, просто введите команду /help")
