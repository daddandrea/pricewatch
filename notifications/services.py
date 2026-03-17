from decimal import Decimal
from tracker.models import Coin

def check_alert(coin: Coin, price: Decimal) -> bool:
    if coin.alert_above:
        return price > coin.threshold - coin.tolerance
    else:
        return price < coin.threshold + coin.tolerance
