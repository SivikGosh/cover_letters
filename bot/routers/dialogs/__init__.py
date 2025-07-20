__all__ = ('router',)

from aiogram import Router

from .add_letter import dialog as add_letter_dialog
from .delete_letter import dialog as delete_letter_dialog
from .edit_letter import dialog as edit_letter_dialog
from .start import dialog as start_dialog

router = Router()

router.include_routers(
    start_dialog,
    add_letter_dialog,
    edit_letter_dialog,
    delete_letter_dialog,
)
