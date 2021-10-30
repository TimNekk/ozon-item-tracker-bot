import pickle
from datetime import datetime


def get_allowed_users():
    from data.config import ALLOWED_USERS_FILE_NAME

    try:
        with open(ALLOWED_USERS_FILE_NAME, 'r') as f:
            return f.read().split('\n')
    except FileNotFoundError:
        return []


def delete_item(index):
    items = get_items()
    items.pop(index)
    save_item(items)


def update_item_time(index):
    from data.config import TIME_BETWEEN_NOTIFICATIONS

    items = get_items()
    items[index][1] = datetime.now() + TIME_BETWEEN_NOTIFICATIONS
    save_item(items)


def add_item(item):
    items = get_items()
    items.append([item, datetime.now()])
    save_item(items)


def save_item(items):
    from data.config import ITEMS_FILE_PATH

    with open(ITEMS_FILE_PATH, 'wb') as f:
        pickle.dump(items, f)


def get_items():
    from data.config import ITEMS_FILE_PATH

    with open(ITEMS_FILE_PATH, 'rb') as f:
        return pickle.load(f)