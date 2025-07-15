__all__ = ('router',)

from aiogram import Router

from .add_letter import dialog as add_letter_dialog
from .welcome import dialog as welcome_dialog

router = Router()

router.include_routers(welcome_dialog, add_letter_dialog)
