from celery import shared_task

from tracker.models import Coin, PriceSnapshot  # noqa: E402
from tracker.coingecko import fetch_prices  # noqa: E402
from notifications.services import send_telegram_alert  # noqa: E402


@shared_task
def save_price_snapshot():
    coins = list(Coin.objects.all())
    if not coins:
        print("No coins found in db.")
        return

    coin_ids = [coin.coin_id for coin in coins]
    print(f"Fetching prices for: {', '.join(coin_ids)}")

    prices = fetch_prices(coin_ids)

    for coin in coins:
        price = prices.get(coin.coin_id)
        if price is None:
            print(f"  [WARN] Price not found for '{coin.coin_id}', skipping...")
            continue

        print(f"  {coin.name} ({coin.coin_id}): ${price}")
        PriceSnapshot(coin=coin, price=price, notified=send_telegram_alert(coin, price)).save()
