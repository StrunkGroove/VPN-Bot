from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from text import additional_commands, menu_commands, admin_commands
from decorators import exception_handler, exception_handler_v2
from service import service_demo_access_key
from states import UserVIPStates
from db import get_count_users


router = Router()


@router.callback_query(lambda c: c.data == additional_commands["what_next"]["key"])
@exception_handler
async def handle_what_next_callback_query(
    callback_query: types.CallbackQuery
) -> None:
    await callback_query.message.answer(
        additional_commands["what_next"]["message"]
    )


@router.callback_query(lambda c: c.data == menu_commands["demo_access_key"]["callback"])
@exception_handler
async def handle_demo_access_key_callback(
    callback_query: types.CallbackQuery
) -> None:
    message_text = await service_demo_access_key(
        user_id=callback_query.from_user.id,
        username=callback_query.from_user.username
    )
    await callback_query.message.answer(message_text)


@router.callback_query(lambda c: c.data == admin_commands["set_user_vip"]["callback"])
@exception_handler_v2
async def handle_set_user_vip_callback(
    callback_query: types.CallbackQuery, 
    state: FSMContext
) -> None:
    await state.set_state(UserVIPStates.waiting_for_user_id)
    await callback_query.message.answer(
        admin_commands["set_user_vip"]["callback_text"]
    )


@router.callback_query(lambda c: c.data == admin_commands["statistics"]["callback"])
@exception_handler
async def handle_admin_statisticks_callback(
    callback_query: types.CallbackQuery, 
) -> None:
    count = await get_count_users()
    await callback_query.message.answer(
        admin_commands["statistics"]["message"].format(
            count=count
        )
    )