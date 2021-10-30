from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("list", "Список товаров"),
            types.BotCommand("add", "Добавить товар"),
            types.BotCommand("delete", "Удалить товар")
        ]
    )
