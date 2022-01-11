from aiogram import types


async def send_welcome(message: types.Message):
    """Хэндлер для приветсвия по команде /start."""
    await message.answer(
        f"Привет, {message.from_user.first_name}\n"
        "Я SHIFT Stonks bot.\nПриятно познакомиться.",
    )
