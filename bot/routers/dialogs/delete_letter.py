from aiogram.enums import ParseMode
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

from bot.states import DeleteLetter
from bot.utils.add_letter import start
from bot.utils.buttons import add_letter
from bot.utils.buttons import approve as approve_button
from bot.utils.delete_letter import approve, get_letter_data
from bot.utils.messages import letter

approve_window = Window(
    letter(),
    approve_button(approve),
    state=DeleteLetter.approve,
    getter=get_letter_data,
    parse_mode=ParseMode.HTML,
)

result_window = Window(
    Const('Письмо удалено.'),
    add_letter(start),
    state=DeleteLetter.result,
    parse_mode=ParseMode.HTML,
)

dialog = Dialog(approve_window, result_window)
