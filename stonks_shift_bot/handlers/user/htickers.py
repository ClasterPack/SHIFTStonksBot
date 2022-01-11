import aiogram.utils.markdown as md
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .moex_requests import Moex


class DateForm(StatesGroup):
    """Форма для даты."""

    date = State()


async def get_history_tickers(message: types.Message):
    """Функция при вызове команды /htickers."""
    await DateForm.date.set()

    await message.reply(
        'Введите дату, для получения списка тикеров:\n'
        'По типу: YYYY-MM-DD',
    )


async def invalid_tickers_h_date(message: types.Message):
    """Функция при неправильно введеной даты."""
    return await message.reply(
        'Неверно указана дата:\n'
        'Правильный формат даты: 2001-01-01 "YYYY-MM-DD".\n'
        'Попробуйте еще раз...',
    )


async def process_data_htickers(message: types.Message, state: FSMContext):
    """Функция возвращает список тикеров или ошибку на отсутствие результата торгов."""
    moex = Moex()
    async with state.proxy() as data:
        data['date'] = message.text
        date = data['date']
        markup = types.ReplyKeyboardRemove()
        list_of_tickers = await moex.get_history_tickers(date)
        custom_reply = ', '.join(list_of_tickers)
        if not list_of_tickers:
            custom_reply = (
                f'На {date} .\n'
                f'Нет информации о торгах.'
            )

    await message.answer(
        md.text(custom_reply),
        reply_markup=markup,
    )
    await state.finish()
