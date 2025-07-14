__all__ = ('router',)

from aiogram import Router

from .welcome import dialog as welcoome_dialog

router = Router()

router.include_routers(welcoome_dialog)
