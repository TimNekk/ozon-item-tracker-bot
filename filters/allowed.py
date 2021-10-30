from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from data.config import ADMINS, ALLOWED_USERS


class IsAllowed(BoundFilter):
    async def check(self, message: types.Message):
        return str(message.chat.id) in ALLOWED_USERS + ADMINS
