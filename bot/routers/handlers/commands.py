from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.states import Welcome

router = Router()


@router.message(CommandStart())  # type: ignore[misc]
async def start(message: Message, dialog_manager: DialogManager) -> None:
    await dialog_manager.start(state=Welcome.state, mode=StartMode.RESET_STACK)
