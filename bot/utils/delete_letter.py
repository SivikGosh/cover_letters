from typing import Any, Dict

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.db_queries import delete_letter, get_letter
from bot.states import DeleteLetter


async def get_letter_data(
    dialog_manager: DialogManager,
    **kwargs: Any
) -> Dict[str, str]:

    assert dialog_manager.event.from_user is not None
    letter = get_letter(dialog_manager.event.from_user.id)

    assert letter is not None
    data = {'title': letter[1], 'text': letter[2]}

    dialog_manager.dialog_data.update(data)

    return data


async def start(
    callback_query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    await dialog_manager.done()
    await dialog_manager.start(DeleteLetter.approve)


async def approve(
    callback_query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:

    assert dialog_manager.event.from_user is not None
    user_id = dialog_manager.event.from_user.id

    letter = dialog_manager.dialog_data['title']

    delete_letter(user_id, letter)

    await dialog_manager.next()
