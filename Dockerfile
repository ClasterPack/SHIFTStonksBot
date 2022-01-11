FROM library/python:3.9-slim

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install --no-install-recommends -y build-essential

RUN mkdir -p /shift_stonks_bot
WORKDIR /shift_stonks_bot

COPY . /shift_stonks_bot
RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install

CMD python -m stonks_shift_bot.bot