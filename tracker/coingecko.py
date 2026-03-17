from decimal import Decimal
import os
import sys
import django
import httpx
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pricewatch.settings")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

django.setup()

from tracker.models import Coin, PriceSnapshot  # noqa: E402
from notifications.services import check_alert  # noqa: E402

COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price"
API_KEY = os.environ["COINGECKO_API_KEY"]


def fetch_prices(coin_ids: list[str]) -> dict[str, Decimal]:
    response = httpx.get(
        COINGECKO_API,
        params={"ids": ",".join(coin_ids), "vs_currencies": "usd"},
        headers={"x-cg-demo-api-key": API_KEY},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    return {coin_id: Decimal(str(data[coin_id]["usd"])) for coin_id in coin_ids if coin_id in data}

def main() -> None:
    coins = list(Coin.objects.all())
    if not coins:
        print("Nessuna moneta trovata nel database.")
        return

    coin_ids = [coin.coin_id for coin in coins]
    print(f"Recupero prezzi per: {', '.join(coin_ids)}")

    prices = fetch_prices(coin_ids)

    snapshots = []
    for coin in coins:
        price = prices.get(coin.coin_id)
        if price is None:
            print(f"  [WARN] Prezzo non trovato per '{coin.coin_id}', salto.")
            continue
        snapshots.append(PriceSnapshot(coin=coin, price=price))
        print(f"  {coin.name} ({coin.coin_id}): ${price}")
        check_alert(coin, price)

    PriceSnapshot.objects.bulk_create(snapshots)


if __name__ == "__main__":
    main()
