from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.db_queries import create_database
from bot.states import Welcome
from bot.utils.common import letter_exists

router = Router()


@router.message(CommandStart())  # type: ignore[misc]
async def start(message: Message, dialog_manager: DialogManager) -> None:

    assert message.from_user is not None
    user_id = message.from_user.id

    create_database(user_id)

    state = (
        Welcome.show_letter
        if letter_exists(user_id)
        else Welcome.add_letter
    )

    await dialog_manager.start(state=state, mode=StartMode.RESET_STACK)
