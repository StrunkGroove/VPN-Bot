from aiogram.fsm.state import State, StatesGroup


class UserVIPStates(StatesGroup):
    waiting_for_user_id = State()