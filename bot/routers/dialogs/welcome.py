from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

from bot.states import Welcome
from bot.utils.add_letter import start

welcome_window = Window(
    Const('Ты можешь добавить письмо.'),
    Button(Const('Добавить'), 'add_letter', start),
    state=Welcome.state,
)

dialog = Dialog(welcome_window)
