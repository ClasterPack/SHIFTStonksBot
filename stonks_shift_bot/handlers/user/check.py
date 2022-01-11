import logging

import aiogram.utils.markdown as md
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from .moex_requests import Moex


class CheckForm(StatesGroup):
    """Форма для тикера."""

    ticker = State()


async def get_price(message: types.Message):
    """Функция при вызове /check ."""
    await CheckForm.ticker.set()

    await message.reply('Введите тикер:')


async def cancel_handler(message: types.Message, state: FSMContext):
    """Позволяет пользователю отменить любые действия , действует в любой команде бота."""
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Canceling state %r', current_state)
    await state.finish()
    await message.reply('Cancelled.', reply_markup=types.ReplyKeyboardRemove())


async def process_ticker_invalid(message: types.Message):
    """Функция при неверном формате тикера."""
    return await message.reply('Тикер должен состоять из букв.')


async def process_invalid_ticker(message: types.Message):
    """Функция при отсутствии тикера в iss.moex.com."""
    return await message.reply(
        'Тикер: не найден, попробуй ещё.\n'
        'Или найди нужный в "/tickers".',
    )


async def process_ticker(message: types.Message, state: FSMContext):
    """Функция возвращающая тикер, короткое имя организации, цену и вилаюту."""
    moex = Moex()
    async with state.proxy() as data:
        data['ticker'] = message.text
        ticker = data['ticker'].upper()
        markup = types.ReplyKeyboardRemove()
        ticker_price = await moex.get_price(ticker)
        await message.answer(
            md.text(
                f'{ticker_price[0]}\n'
                f'{ticker_price[1]}\n'
                f'{ticker_price[2]} {ticker_price[3]}',
            ),
            reply_markup=markup,
        )
    await state.finish()
