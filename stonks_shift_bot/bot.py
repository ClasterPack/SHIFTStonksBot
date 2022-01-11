import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode
from data import config


def on_startup():
    """Старт работы бота."""
    import filters
    import handlers
    filters.setup(dp)
    handlers.errors.setup(dp)
    handlers.user.setup(dp)
    logging.basicConfig(level=logging.WARNING)


if __name__ == '__main__':
    bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    on_startup()
    executor.start_polling(dp)
