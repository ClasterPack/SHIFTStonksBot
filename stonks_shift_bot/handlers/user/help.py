from aiogram import types
from utils.misc import rate_limit


@rate_limit(5, 'help')
async def bot_help(message: types.Message):
    """Функция при вызове /help ."""
    await message.answer(
        'Список команд:\n'
        '/start - Приветственное сообщение\n'
        '/check - проверить цену на MOEX по тикеру.\n'
        '/tickers - запросить список тикеров MOEX.\n'
        '/htickers  - запросить тикеры закрытых торгов по дате в MOEX.\n '
        '/history  - запросить цену закрытия торгов по тикеру на необходимую дату.\n'
        '/help - список команд.',
    )
