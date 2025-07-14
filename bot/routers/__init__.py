__all__ = ('router',)

from aiogram import Router

from .dialogs import router as dialogs_router
from .handlers import router as handlers_router

router = Router()

router.include_routers(handlers_router, dialogs_router)
