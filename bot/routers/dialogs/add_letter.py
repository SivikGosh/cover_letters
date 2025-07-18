from aiogram.enums import ParseMode
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Next
from aiogram_dialog.widgets.text import Const

from bot.states import AddLetter
from bot.utils.add_letter import approve, get_input_data
from bot.utils.buttons import approve as approve_button
from bot.utils.buttons import edit_letter
from bot.utils.edit_letter import start
from bot.utils.messages import letter, letter_saved

title_window = Window(
    Const('Введи заголовок:'),
    TextInput('title', on_success=Next()),
    state=AddLetter.title,
)

text_window = Window(
    Const('Введи текст:'),
    TextInput('text', on_success=Next()),
    state=AddLetter.text,
)

approve_window = Window(
    letter(),
    approve_button(approve),
    state=AddLetter.approve,
    getter=get_input_data,
    parse_mode=ParseMode.HTML,
)

result_window = Window(
    letter_saved(),
    letter(),
    edit_letter(start),
    state=AddLetter.result,
    getter=get_input_data,
    parse_mode=ParseMode.HTML,
)

dialog = Dialog(title_window, text_window, approve_window, result_window)
