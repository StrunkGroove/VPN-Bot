import logging
from uuid import uuid4
from typing import Callable

from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from text import text
from exceptions import DatabaseExceptions


def exception_handler(func: Callable) -> Callable:
    async def wrapper(message: Message, *args, **kwargs) -> None:
        try:
            return await func(message)
        except (DatabaseExceptions, Exception) as e:
            uuid = uuid4()
            logging.exception(f"{uuid}: {e}")
            await message.answer(text["exceptions"].format(
                exceptions_token=uuid
            ))
    return wrapper


def exception_handler_v2(func: Callable) -> Callable:
    async def wrapper(
        message: Message, 
        state: FSMContext, 
        *args, 
        **kwargs
    ) -> None:
        try:
            return await func(message, state)
        except (DatabaseExceptions, Exception) as e:
            uuid = uuid4()
            logging.exception(f"{uuid}: {e}")
            await message.answer(text["exceptions"].format(
                exceptions_token=uuid
            ))
    return wrapper


def db_exception_handler(func: Callable) -> Callable:
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Exception in func {func.__name__}: {str(e)}")
            raise DatabaseExceptions()
    return wrapper