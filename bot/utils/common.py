from typing import Any, Dict

from aiogram_dialog import DialogManager

from bot.db_queries import get_letter


def letter_exists(user_id: int) -> bool:
    return True if get_letter(user_id) else False


async def get_letter_data(
    dialog_manager: DialogManager,
    **kwargs: Any
) -> Dict[str, str]:

    assert dialog_manager.event.from_user is not None
    user_id = dialog_manager.event.from_user.id

    letter = get_letter(user_id)
    assert letter is not None, 'Письмо не найдено.'
    _, title, text = letter

    return {'title': title, 'text': text}
