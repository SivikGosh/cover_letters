from aiogram.enums import ParseMode
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot.states import Welcome
from bot.utils.add_letter import start as start_add_letter
from bot.utils.buttons import edit_letter
from bot.utils.common import get_letter_data
from bot.utils.edit_letter import start as start_edit_letter
from bot.utils.messages import letter

add_letter_window = Window(
    Const('Ты можешь добавить письмо.'),
    Button(Const('Добавить'), 'add_letter', start_add_letter),
    state=Welcome.add_letter,
)

show_letter_window = Window(
    letter(),
    edit_letter(start_edit_letter),
    state=Welcome.show_letter,
    getter=get_letter_data,
    parse_mode=ParseMode.HTML
)

dialog = Dialog(add_letter_window, show_letter_window)
