import re

from aiogram import types
from aiogram.dispatcher.filters import Filter


class IsDate(Filter):
    """Фильтр для валидного формата даты."""

    key = 'is_date'

    async def check(self, message: types.Message):
        """Верный формат даты."""
        if re.match('\d\d\d\d-\d\d-\d\d', message.text):
            return True
        return False


class NotDate(Filter):
    """Фильтр для неверного формата даты."""

    key = 'not_date'

    async def check(self, message: types.Message):
        """Неверный формат даты."""
        if re.match('\d\d\d\d-\d\d-\d\d', message.text):
            return False
        return True
