## Shift Final:

Телеграм бот для получения котировок акций с Моковской биржи по тикеру акции.


Настроить репозиторий:
```shell script
git clone https://gitlab.com/shift-python/tolstopyatov/shift_stonks_bot.git shift_stonks_bot
cd shift_stonks_bot
```
   
## Рабочее окружение
Для начала разработки необходимо настроить рабочее окружение. Нам понадобятся следующие системные зависимости: 
- [python](https://www.python.org/downloads/) версии 3.9 или выше
- менеджер зависимостей [poetry](https://python-poetry.org/docs/#installation) версии 1.0 или выше

## Запуск

Подключение виртуального окружения
```shell script
poetry shell
```

TelegramBot:

- [SHIFT_my_moexchange_bot](https://t.me/SHIFT_my_moexchange_bot)

Установить зависимости. Зависимости установятся в виртуальное окружение.
```shell script
poetry install 
```

Из виртуального окружения сервис запускается командой

- Чтобы бот работал надо задать stonks_shift_bot рабочей директорией
```shell script
python -m stonks_shift_bot.bot
```

