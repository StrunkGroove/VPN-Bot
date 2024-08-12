from aiogram import Router

from .callbacks import router as callbacks_router
from .commands import router as commands_router


router = Router()
router.include_routers(
    callbacks_router,
    commands_router
)
