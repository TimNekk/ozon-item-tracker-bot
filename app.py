import asyncio
import os
import pickle

import aioschedule
from aiogram import executor

from data.config import ALLOWED_USERS_FILE_NAME, ITEMS_FILE_PATH
from loader import dp
import middlewares, filters, handlers
from utils.notifier import on_startup_notify_admins
from utils.parser import check_items
from utils.set_bot_commands import set_default_commands


async def scheduler():
    aioschedule.every(3).seconds.do(check_items)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(dispatcher):
    # Create Scheduler
    asyncio.create_task(scheduler())

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify_admins(dispatcher)

    if not os.path.isfile(ALLOWED_USERS_FILE_NAME):
        with open(ALLOWED_USERS_FILE_NAME, 'wb'):
            pass

    if not os.path.isfile(ITEMS_FILE_PATH):
        with open(ITEMS_FILE_PATH, 'wb') as f:
            pickle.dump([], f)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

