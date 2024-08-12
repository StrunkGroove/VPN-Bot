from aiogram import types, Router
from aiogram.fsm.context import FSMContext

from db.func import set_user_flag
from .states import UserVIPStates
from .text import set_user_vip_text


router = Router()

@router.message(UserVIPStates.waiting_for_user_id)
async def process_user_id(message: types.Message, state: FSMContext):
    await set_user_flag(
        user_id=message.from_user.id, 
        flag="is_vip"
    )
    await message.answer(set_user_vip_text["message"].format(
        user=message.text
    ))
    await state.clear()