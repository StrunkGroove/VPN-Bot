import logging
from functools import wraps

logger = logging.getLogger("vpn_bot")


def catch_errors(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Ошибка в обработчике {func.__name__}: {e}", exc_info=True)
            if args:
                message = args[0]
                try:
                    await message.answer("Произошла ошибка, попробуйте позже.")
                except Exception:
                    pass

    return wrapper
