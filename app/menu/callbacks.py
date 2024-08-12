from aiogram import Router, types

from shared.decorators import handler_exception
from .service import service_demo_access_key
from .text import (
    demo_access_text, 
    what_next_text
)


router = Router()

@router.callback_query(lambda c: c.data == demo_access_text["callback"])
@handler_exception
async def handle_demo_access_callback(
    callback_query: types.CallbackQuery
) -> None:
    message_text = await service_demo_access_key(
        user_id=callback_query.from_user.id,
        username=callback_query.from_user.username
    )
    await callback_query.message.answer(message_text)


@router.callback_query(lambda c: c.data == what_next_text["key"])
@handler_exception
async def handle_what_next_callback_query(
    callback_query: types.CallbackQuery
) -> None:
    await callback_query.message.answer(
        what_next_text["message"]
    )