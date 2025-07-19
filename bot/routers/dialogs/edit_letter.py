from aiogram.enums import ParseMode
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Next
from aiogram_dialog.widgets.text import Const

from bot.states import EditLetter
from bot.utils.buttons import approve as approve_button
from bot.utils.buttons import edit_letter, skip_step
from bot.utils.edit_letter import approve, get_input_data, skip, start
from bot.utils.messages import letter, letter_saved

title_window = Window(
    Const('Введи заголовок:'),
    TextInput('title', on_success=Next()),
    skip_step(skip),
    state=EditLetter.title,
)

text_window = Window(
    Const('Введи текст:'),
    TextInput('text', on_success=Next()),
    skip_step(skip),
    state=EditLetter.text,
)

approve_window = Window(
    letter(),
    approve_button(approve),
    state=EditLetter.approve,
    getter=get_input_data,
    parse_mode=ParseMode.HTML,
)

result_window = Window(
    letter_saved(),
    letter(),
    edit_letter(start),
    state=EditLetter.result,
    getter=get_input_data,
    parse_mode=ParseMode.HTML,
)

dialog = Dialog(title_window, text_window, approve_window, result_window)
