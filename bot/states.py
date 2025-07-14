from aiogram.filters.state import State, StatesGroup


class Welcome(StatesGroup):  # type: ignore[misc]
    state = State()
