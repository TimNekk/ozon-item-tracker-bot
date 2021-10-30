import pickle
import re

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.file_manager import add_item
from filters import IsAllowed
from loader import dp


@dp.message_handler(IsAllowed(), commands='add')
async def bot_add(message: types.Message, state: FSMContext):
    await state.set_state('add')
    await message.answer('Отправьте ссылку на файл')


@dp.message_handler(state='add')
async def bot_save(message: types.Message, state: FSMContext):
    item = re.search(r"ozon\.ru/product/.+/", message.text)

    if item:
        item = item.group(0)
        add_item(item)
        text = f'<b>Добавлен новый товар</b>\n{item}'
    else:
        text = f'Неверная ссылка'

    await message.answer(text)
    await state.finish()
