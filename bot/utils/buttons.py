from typing import Awaitable, Callable

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const


def edit_letter(
    func: Callable[[CallbackQuery, Button, DialogManager], Awaitable[None]]
) -> Button:
    return Button(Const('Редактировать'), 'edit_letter', func)


def skip_step(
    func: Callable[[CallbackQuery, Button, DialogManager], Awaitable[None]]
) -> Button:
    return Button(Const('Пропустить'), 'skip', func)


def approve(
    func: Callable[[CallbackQuery, Button, DialogManager], Awaitable[None]]
) -> Button:
    return Button(Const('Подтвердить'), 'approve', func)
