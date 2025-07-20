from aiogram.fsm.state import State, StatesGroup


class Welcome(StatesGroup):  # type: ignore[misc]
    add_letter = State()
    show_letter = State()


class AddLetter(StatesGroup):  # type: ignore[misc]
    title = State()
    text = State()
    alias = State()
    approve = State()
    result = State()


class EditLetter(StatesGroup):  # type: ignore[misc]
    title = State()
    text = State()
    alias = State()
    approve = State()
    result = State()


class DeleteLetter(StatesGroup):  # type: ignore[misc]
    approve = State()
    result = State()
