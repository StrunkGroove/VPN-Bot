from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from db.func import get_count_users
from shared.decorators import (
    handler_exception, 
    handler_exception_v2
)
from .text import set_user_vip_text, statistics_text
from .states import UserVIPStates


router = Router()

@router.callback_query(lambda c: c.data == set_user_vip_text["callback"])
@handler_exception_v2
async def handle_set_user_vip_callback(
    callback_query: types.CallbackQuery, 
    state: FSMContext
) -> None:
    await state.set_state(UserVIPStates.waiting_for_user_id)
    await callback_query.message.answer(
        set_user_vip_text["callback_text"]
    )


@router.callback_query(lambda c: c.data == statistics_text["callback"])
@handler_exception
async def handle_admin_statistics_callback(
    callback_query: types.CallbackQuery, 
) -> None:
    count = await get_count_users()
    await callback_query.message.answer(
        statistics_text["message"].format(
            count=count
        )
    )