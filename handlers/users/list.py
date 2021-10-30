from aiogram import types

from data.file_manager import get_items
from filters import IsAllowed
from loader import dp


@dp.message_handler(IsAllowed(), commands='list')
async def bot_add(message: types.Message):
    items = get_items()
    text = '<b>Отслеживаемые товары: </b>\n\n'

    for index, item in enumerate(items):
        text += f"{index + 1}) {item[0]}\n"

    await message.answer(text, disable_web_page_preview=False)