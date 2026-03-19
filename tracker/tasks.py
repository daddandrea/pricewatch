from celery import shared_task

from tracker.models import Coin, PriceSnapshot #noqa: E402
from tracker.coingecko import fetch_prices     #noqa: E402 
from notifications.services import check_alert #noqa: E402

@shared_task
def save_price_snapshot():
    coins = list(Coin.objects.all())
    if not coins:
        print("No coins found in db.")
        return

    coin_ids = [coin.coin_id for coin in coins]
    print(f"Fetching prices for: {", ".join(coin_ids)}")

    prices = fetch_prices(coin_ids)

    snapshots = []
    for coin in coins:
        price = prices.get(coin.coin_id)
        if price is None:
            print(f"  [WARN] Price not found for '{coin.coin_id}', skipping...")
            continue

        snapshots.append(PriceSnapshot(coin=coin, price=price))
        print(f"  {coin.name} ({coin.coin_id}): ${price}")

        check_alert(coin, price)

    PriceSnapshot.objects.bulk_create(snapshots)
