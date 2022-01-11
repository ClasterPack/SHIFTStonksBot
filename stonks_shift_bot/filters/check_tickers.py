from aiogram import types
from aiogram.dispatcher.filters import Filter
from handlers.user.moex_requests import Moex


class IsTicker(Filter):
    """Фильтр для проверки тикера на вхождение."""

    key = 'ticker'

    async def check(self, message: types.Message):
        """Результат проверки тикера."""
        moex = Moex()
        ticker = message.text
        answer = await moex.check_ticker(ticker)
        if answer:
            return True
        if not answer:
            return False


class NotTicker(Filter):
    """Фильтры при отсутствии тикера ."""

    key = 'not_ticker'

    async def check(self, message: types.Message):
        """Результат проверки тикера."""
        moex = Moex()
        ticker = message.text
        answer = await moex.check_ticker(ticker)
        if answer:
            return False
        if not answer:
            return True
