from typing import Any, Dict

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.states import AddLetter
from bot.utils.db_queries import add_letter


async def input_data(
    dialog_manager: DialogManager,
    **kwargs: Any
) -> Dict[str, str]:
    data = {
        'title': dialog_manager.find('title').get_value(),
        'text': dialog_manager.find('text').get_value(),
    }
    dialog_manager.dialog_data.update(data)
    return data


async def start(
    callback_query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    await dialog_manager.done()
    await dialog_manager.start(AddLetter.title)


async def approve(
    callback_query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    user_id = dialog_manager.event.from_user.id
    title = dialog_manager.dialog_data['title']
    text = dialog_manager.dialog_data['text']
    add_letter(user_id, title, text)
    await dialog_manager.next()
