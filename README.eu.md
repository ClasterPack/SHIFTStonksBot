***
**_Read this in other languages: [English](README.eu.md), [Русский](README.md)_**
***

## Shift Final
(The final training project of the intensive):

Telegram bot for receiving stock quotes from the MOEX by stock ticker.

Setup repo:
```shell script
git clone https://gitlab.com/shift-python/tolstopyatov/shift_stonks_bot.git shift_stonks_bot
cd shift_stonks_bot
```
   
## Working environment:
We need the following system dependencies:
- [python](https://www.python.org/downloads/release/python-390/) version 3.9 
- Dependency manager [poetry](https://python-poetry.org/docs/#installation) version 1.0
- 
Environment setup:
```shell script
poetry shell
```

TelegramBot:

- [SHIFT_my_moexchange_bot](https://t.me/SHIFT_my_moexchange_bot)


Install dependencies. Dependencies will be installed in the virtual environment.
```shell script
poetry install 
```

From the virtual environment, the service is started by the command:
```shell script
python -m stonks_shift_bot.bot
```
- For the bot to work, you need to set stonks_shift_bot as the working directory
