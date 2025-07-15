from aiogram.enums import ParseMode
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot.states import Welcome
from bot.utils.add_letter import start
from bot.utils.common import get_letter_data
from bot.utils.messages import letter

add_letter_window = Window(
    Const('Ты можешь добавить письмо.'),
    Button(Const('Добавить'), 'add_letter', start),
    state=Welcome.add_letter,
)

show_letter_window = Window(
    letter(),
    state=Welcome.show_letter,
    getter=get_letter_data,
    parse_mode=ParseMode.HTML
)

dialog = Dialog(add_letter_window, show_letter_window)
