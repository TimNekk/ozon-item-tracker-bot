from datetime import timedelta

from environs import Env

from data import file_manager

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

ALLOWED_USERS_FILE_NAME = 'allowed_users.txt'
ALLOWED_USERS = file_manager.get_allowed_users()

ITEMS_FILE_PATH = 'items.txt'

TIME_BETWEEN_NOTIFICATIONS = timedelta(minutes=30)
