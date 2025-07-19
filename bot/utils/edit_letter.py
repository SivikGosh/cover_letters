from typing import Any, Dict

from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.db_queries import get_letter, update_letter
from bot.states import EditLetter


async def get_input_data(
    dialog_manager: DialogManager,
    **kwargs: Any
) -> Dict[str, str]:

    start_data = dialog_manager.start_data

    if isinstance(start_data, dict):
        old_title = start_data.get('old_title')
        old_text = start_data.get('old_text')
    else:
        old_title, old_text = None, None

    new_title = dialog_manager.find('title')
    new_text = dialog_manager.find('text')

    if new_title is None or new_text is None:
        raise ValueError('Введённые данные где-то потерялись.')

    title = (
        new_title.get_value()
        if new_title.get_value() is not None
        else old_title
    )
    text = (
        new_text.get_value()
        if new_text.get_value() is not None
        else old_text
    )

    if title is None or text is None:
        raise ValueError('Итоговые данные где-то потерялись.')

    data = {'title': title, 'text': text}

    dialog_manager.dialog_data.update(data)

    return data


async def start(
    callback_query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:

    await dialog_manager.done()

    assert dialog_manager.event.from_user is not None
    letter = get_letter(dialog_manager.event.from_user.id)

    assert letter is not None
    data = {'old_title': letter[1], 'old_text': letter[2]}

    await dialog_manager.start(EditLetter.title, data)


async def skip(
    callback_query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:
    await dialog_manager.next()


async def approve(
    callback_query: CallbackQuery,
    button: Button,
    dialog_manager: DialogManager,
) -> None:

    assert dialog_manager.event.from_user is not None
    user_id = dialog_manager.event.from_user.id

    title = dialog_manager.dialog_data['title']
    text = dialog_manager.dialog_data['text']

    update_letter(user_id, title, text)

    await dialog_manager.next()
