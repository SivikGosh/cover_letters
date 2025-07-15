from asyncio import run
from logging import DEBUG, basicConfig

from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs

from bot.config import TOKEN
from bot.routers import router


async def main() -> None:

    basicConfig(level=DEBUG)

    if TOKEN is None:
        raise RuntimeError('Токен не установлен.')
    bot = Bot(TOKEN)

    dp = Dispatcher()
    dp.include_router(router)
    setup_dialogs(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main())
