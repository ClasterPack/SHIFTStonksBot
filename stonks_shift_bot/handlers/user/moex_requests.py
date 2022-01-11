import aiohttp

moex = 'https://iss.moex.com/'
root_latest = (
    'iss/engines/stock/markets/shares/boards/TQBR/securities.json'
)
root_history = (
    'iss/history/engines/stock/markets/shares/securities.json?date='
)
settings_ticker = (
    '?iss.meta=off&iss.only=securities&securities.columns=SECID'
)
settings_latest_price = (
    '?iss.meta=off&iss.only=securities&securities.columns=SECID,SHORTNAME,PREVPRICE,FACEUNIT'
)
history_params = (
    '&iss.meta=off&iss.only=history&history.columns=SECID,SHORTNAME,TRADEDATE,LEGALCLOSEPRICE'
)
history_params_ticker = (
    '&iss.meta=off&iss.only=history&history.columns=SECID'
)


class Moex:
    """Класс для работы с MOEX ."""

    def __init__(self):
        """Задаем урлы."""
        self.tickers_url = f'{moex}{root_latest}{settings_ticker}'
        self.prices_url = f'{moex}{root_latest}{settings_latest_price}'
        self.history_params = history_params
        self.history_params_ticker = history_params_ticker
        self.history_url = f'{moex}{root_history}'
        self.tickers = []

    async def get_tickers(self):
        """Функция для получения списка тикеров с последних торгов."""
        self.tickers = []
        async with aiohttp.ClientSession() as session:
            async with session.get(self.tickers_url) as response:
                try:
                    resp = await response.json()
                except Exception as ex:
                    with open('logger.txt', 'a') as logger:
                        logger.write(f'{ex}\n')
                        return 'Упс. Что-то пошло не так...'
                for exist_ticker in resp['securities']['data']:
                    self.tickers.append(exist_ticker[0])
                return self.tickers

    async def get_history_tickers(self, date):
        """Функция для получения тикеров по дате торгов."""
        self.tickers = []
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.history_url}{date}{history_params_ticker}') as response:
                try:
                    resp = await response.json()
                except Exception as ex:
                    with open('logger.txt', 'a') as logger:
                        logger.write(f'{ex}\n')
                        return 'Упс. Что-то пошло не так...'
                for history_ticker in resp['history']['data']:
                    self.tickers.append(history_ticker[0])
                return self.tickers

    async def check_ticker(self, ticker):
        """Функция на проверку есть ли тикер в списке тикеров последних торгов."""
        ticker = ticker.upper()
        self.tickers = await self.get_tickers()
        if ticker in self.tickers:
            return True
        if ticker not in self.tickers:
            return False

    async def get_price(self, ticker):
        """Функция получения цены тикера."""
        ticker = ticker.upper()
        async with aiohttp.ClientSession() as session:
            async with session.get(self.prices_url) as response:
                try:
                    response = await response.json()
                except Exception as ex:
                    with open('logger.txt', 'a') as logger:
                        logger.write(f'{ex}\n')
                    return 'Упс. Что-то пошло не так...'
                for exist_ticker in response['securities']['data']:
                    if exist_ticker[0] == ticker:
                        return exist_ticker
                return False

    async def check_history_ticker(self, ticker, date):
        """Функция проверки тикера в списке тикеров на указанную дату."""
        ticker = ticker.upper()
        self.tickers = await self.get_history_tickers(date)
        if ticker in self.tickers:
            return True
        if ticker not in self.tickers:
            return False

    async def get_history_price(self, ticker, date):
        """Функция возвращающая цену тикера (LEGALCLOSEPRICE) на указанную дату ."""
        ticker = ticker.upper()
        self.tickers = []
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.history_url}{date}{history_params}') as response:
                try:
                    resp = await response.json()
                except Exception as ex:
                    with open('logger.txt', 'a') as logger:
                        logger.write(f'{ex}\n')
                    return 'Упс. Что-то пошло не так...'
                for history_ticker in resp['history']['data']:
                    if history_ticker[0] == ticker:
                        return history_ticker
                return False
