from aiogram.enums import ParseMode
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

from bot.states import Welcome
from bot.utils.add_letter import start as start_add_letter
from bot.utils.buttons import add_letter, delete_letter, edit_letter
from bot.utils.common import get_letter_data
from bot.utils.delete_letter import start as start_delete_letter
from bot.utils.edit_letter import start as start_edit_letter
from bot.utils.messages import letter

add_letter_window = Window(
    Const('Ты можешь добавить письмо.'),
    add_letter(start_add_letter),
    state=Welcome.add_letter,
)

show_letter_window = Window(
    letter(),
    edit_letter(start_edit_letter),
    delete_letter(start_delete_letter),
    state=Welcome.show_letter,
    getter=get_letter_data,
    parse_mode=ParseMode.HTML
)

dialog = Dialog(add_letter_window, show_letter_window)
