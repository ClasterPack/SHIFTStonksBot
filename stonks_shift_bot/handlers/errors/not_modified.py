from aiogram import types
from aiogram.utils import exceptions


async def message_not_modified(update: types.Update, error: exceptions.MessageNotModified):
    """Не модифицированное сообщение, error handler."""
    return True


async def message_to_delete_not_found(update: types.Update, error: exceptions.MessageToDeleteNotFound):
    """Удаленное сообщение, error handler."""
    return True
