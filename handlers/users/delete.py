import re

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.file_manager import add_item, delete_item, get_items
from filters import IsAllowed
from loader import dp


@dp.message_handler(IsAllowed(), commands='delete')
async def bot_delete(message: types.Message, state: FSMContext):
    await state.set_state('delete')
    await message.answer('Введите номер товара для удаления')


@dp.message_handler(state='delete')
async def bot_del(message: types.Message, state: FSMContext):
    items = get_items()
    if message.text.isdigit() and 0 <= int(message.text) - 1 < len(items) and items:

        delete_item(int(message.text) - 1)
        text = f'<b>Товар номер {message.text} удален</b>'
    else:
        text = f'Неверный номер'

    await message.answer(text)
    await state.finish()
