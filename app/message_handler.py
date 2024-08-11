from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from states import UserVIPStates
from text import admin_commands
from db import set_user_flag

router = Router()


@router.message(UserVIPStates.waiting_for_user_id)
async def process_user_id(message: types.Message, state: FSMContext):
    await set_user_flag(
        user_id=message.from_user.id, 
        flag="is_vip"
    )
    await message.answer(admin_commands["set_user_vip"]["message"].format(
        user=message.text
    ))
    await state.clear()