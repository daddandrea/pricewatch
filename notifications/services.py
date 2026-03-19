from decimal import Decimal
from tracker.models import Coin

import os
import httpx

TELEGRAM_API = "https://api.telegram.org/bot<TOKEN>/sendMessage"

def _should_notify(coin: Coin, price: Decimal) -> bool:
    if coin.alert_above:
        return price > coin.threshold - coin.tolerance
    else:
        return price < coin.threshold + coin.tolerance


def send_telegram_alert(coin: Coin, price: Decimal) -> bool:
    if not _should_notify(coin, price):
        return False

    CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
    BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

    url = TELEGRAM_API.replace("<TOKEN>", BOT_TOKEN)

    response = httpx.get(
        url,
        params={
            "chat_id": CHAT_ID,
            "text": f"{coin.name} is at '{price}'!"
        },
        timeout=10,
    )

    return response.is_success
