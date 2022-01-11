from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandHelp, Text
from filters.check_date import IsDate, NotDate
from filters.check_tickers import IsTicker, NotTicker

from .check import (
    CheckForm,
    cancel_handler,
    get_price,
    process_invalid_ticker,
    process_ticker,
    process_ticker_invalid,
)
from .help import bot_help
from .history_check import (
    HistoryForm,
    get_history_price,
    invalid_date,
    invalid_history_ticker,
    process_history_date,
    process_history_ticker,
)
from .htickers import DateForm, get_history_tickers, invalid_tickers_h_date, process_data_htickers
from .start import send_welcome
from .tickers import check_tickers


def setup(dp: Dispatcher):
    """Функции диспатчера."""
    dp.bind_filter(IsDate)
    dp.bind_filter(NotDate)
    dp.bind_filter(IsTicker)
    dp.bind_filter(NotTicker)
    dp.register_message_handler(
        send_welcome,
        commands=['start', 'старт'],
    )
    dp.register_message_handler(
        bot_help,
        CommandHelp(),
    )
    dp.register_message_handler(
        check_tickers,
        commands=['tickers'],
    )
    dp.register_message_handler(
        get_price,
        commands=['check'],
    )
    dp.register_message_handler(
        cancel_handler,
        state="*",
        commands='cancel',
    )
    dp.register_message_handler(
        cancel_handler,
        Text(
            equals='cancel', ignore_case=True,
        ),
        state='*',
    )
    dp.register_message_handler(
        process_ticker_invalid,
        lambda message: not message.text.isalpha(),
        state=CheckForm.ticker,
    )
    dp.register_message_handler(
        process_invalid_ticker,
        NotTicker(),
        state=CheckForm.ticker,
    )
    dp.register_message_handler(
        process_ticker,
        IsTicker(),
        lambda message: message.text.isalpha(),
        state=CheckForm.ticker,
    )
    dp.register_message_handler(
        get_history_price,
        commands=['history'],
    )
    dp.register_message_handler(
        invalid_date,
        NotDate(),
        state=HistoryForm.date,
    )
    dp.register_message_handler(
        process_history_date,
        IsDate(),
        state=HistoryForm.date,
    )
    dp.register_message_handler(
        invalid_history_ticker,
        lambda message: not message.text.isalpha(),
        state=HistoryForm.history_ticker,
    )
    dp.register_message_handler(
        process_history_ticker,
        lambda message: message.text.isalpha(),
        state=HistoryForm.history_ticker,
    )
    dp.register_message_handler(
        get_history_tickers,
        commands=['htickers'],
    )
    dp.register_message_handler(
        invalid_tickers_h_date,
        NotDate(),
        state=DateForm.date,
    )
    dp.register_message_handler(
        process_data_htickers,
        IsDate(),
        state=DateForm.date,
    )
