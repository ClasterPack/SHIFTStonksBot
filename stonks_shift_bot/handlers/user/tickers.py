from aiogram import types

from .moex_requests import Moex


async def check_tickers(message: types.Message):
    """Функция вызова списка тикеров."""
    if message.text.lower() == "/tickers":
        moex = Moex()
        ticker_list = await moex.get_tickers()
        await message.answer(', '.join(ticker_list))
    else:
        await message.answer(
            'Неверная команда.\n'
            'Проверь список команд. "/help"',
        )
