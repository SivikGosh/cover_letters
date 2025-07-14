from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

from bot.states import Welcome

welcome_window = Window(
    Const('Бот успешно запущен. И пока на этом всё. Продолжение следует.'),
    state=Welcome.state,
)

dialog = Dialog(welcome_window)
