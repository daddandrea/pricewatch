from decimal import Decimal
import os
import httpx

COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price"
API_KEY = os.environ["COINGECKO_API_KEY"]


def fetch_prices(coin_ids: list[str]) -> dict[str, Decimal]:
    response = httpx.get(
        COINGECKO_API,
        params={
            "ids": ",".join(coin_ids),
            "vs_currencies": "usd"
        },
        headers={"x-cg-demo-api-key": API_KEY},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    return {coin_id: Decimal(str(data[coin_id]["usd"])) for coin_id in coin_ids if coin_id in data}
