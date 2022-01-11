import aiogram.utils.markdown as md
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .moex_requests import Moex


class HistoryForm(StatesGroup):
    """Форма для тикера по дате."""

    date = State()
    history_ticker = State()


async def get_history_price(message: types.Message):
    """Получаем команду /history. обрабатываем, отправляем ответ."""
    await HistoryForm.date.set()

    await message.reply('Введите дату:\n'
                        'По типу: YYYY-MM-DD',
                        )


async def invalid_date(message: types.Message):
    """Функция обработки неверной даты."""
    return await message.reply(
        'Неверно указана дата:\n'
        'Правильный формат даты: 2001-01-01 .\n'
        'Попробуйте еще раз...',
    )


async def process_history_date(message: types.Message, state: FSMContext):
    """
    Функция при введении правильной даты.

    Переходим к следующей форме сохраняем предидущую.
    """
    async with state.proxy() as data:
        data['date'] = message.text

    await HistoryForm.next()
    await state.update_data(date=str(message.text))
    await message.reply('Введите тикер:')


async def invalid_history_ticker(message: types.Message):
    """Функция обработки неверного формата тикера."""
    return await message.reply('Тикер должен состоять из букв.')


async def process_history_ticker(message: types.Message, state: FSMContext):
    """Функция последней обработки запроса возвращающая результат или текст ошибки."""
    moex = Moex()
    markup = types.ReplyKeyboardRemove()
    async with state.proxy() as data:
        date = data['date']
        history_ticker = message.text
        data['history_ticker'] = history_ticker.upper()
        history_tickers_list = await moex.get_history_tickers(date)
        if history_ticker not in history_tickers_list:
            custom_reply = (
                'Тикер не найден попробуй ещё.\n'
                'Посмотрететь список тикеров по дате,\n'
                'можно с помощью команды: "/htickers"\n'
                'И ввести необходимую дату.'
            )
        if not history_tickers_list:
            custom_reply = (
                f'На {date} .\n'
                f'Нет информации о торгах.'
            )
        if await moex.check_history_ticker(history_ticker, date):
            ticker_price = await moex.get_history_price(history_ticker, date)
            data['ticker_price'] = ticker_price
            if type(ticker_price) == list:
                custom_reply = (
                    f'{ticker_price[0]}\n'
                    f'"{ticker_price[1]}"\n'
                    f'{ticker_price[2]}\n'
                    f'{ticker_price[3]} SUR'
                )
            if type(ticker_price) == str:
                custom_reply = ticker_price
    await message.answer(
        md.text(custom_reply),
        reply_markup=markup,
    )

    await state.finish()
