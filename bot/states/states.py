from aiogram.filters.state import State, StatesGroup


class Welcome(StatesGroup):  # type: ignore[misc]
    state = State()


class AddLetter(StatesGroup):  # type: ignore[misc]
    title = State()
    text = State()
    alias = State()
    approve = State()
    result = State()
