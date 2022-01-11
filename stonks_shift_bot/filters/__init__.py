from aiogram import Dispatcher

from .is_admin import AdminFilter


def setup(dp: Dispatcher):
    """Настройка фильтров в диспатчере."""
    dp.filters_factory.bind(AdminFilter)
