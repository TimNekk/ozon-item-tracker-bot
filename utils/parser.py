from datetime import datetime

from requests import Session
from bs4 import BeautifulSoup as BS
import headers_converter

from data.file_manager import get_items, update_item_time
from utils.notifier import notify

headers = headers_converter.convert(
    """user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 YaBrowser/21.9.0.1044 Yowser/2.5 Safari/537.36""")


async def check_items():
    times = get_items()

    for index, item in enumerate(times):
        if datetime.now() < item[1]:
            continue
        
        status, price = is_item_available(f"https://{item[0]}")
        if status:
            update_item_time(index)

            text = f"<b>ДОСТУПНО ЗА: {price.text}</b>\n{item[0]}"
            await notify(text)


def is_item_available(item: str):
    with Session() as sess:
        resp = sess.get(item, headers=headers)

        soup = BS(resp.content, "lxml")

        empty_label = soup.select_one(".c2e1 .c2e2")
        price_label = soup.select_one(".c2h3.c2h9 .c2h5")

        return empty_label is None, price_label
