from aiogram import types

from filters import IsAllowed
from loader import dp


@dp.message_handler(IsAllowed(), commands='start')
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
