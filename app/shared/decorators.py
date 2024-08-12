import logging
from uuid import uuid4
from typing import Callable

from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from .text import exceptions as exceptions_text


def handler_exception(func: Callable) -> Callable:
    async def wrapper(message: Message, *args, **kwargs) -> None:
        try:
            return await func(message)
        except Exception as e:
            uuid = uuid4()
            logging.exception(f"{uuid}: {e}")
            await message.answer(exceptions_text.format(
                exceptions_token=uuid
            ))
    return wrapper


def handler_exception_v2(func: Callable) -> Callable:
    async def wrapper(
        message: Message, 
        state: FSMContext, 
        *args, 
        **kwargs
    ) -> None:
        try:
            return await func(message, state)
        except Exception as e:
            uuid = uuid4()
            logging.exception(f"{uuid}: {e}")
            await message.answer(exceptions_text.format(
                exceptions_token=uuid
            ))
    return wrapper


