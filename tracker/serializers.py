from tracker.models import Coin, PriceSnapshot
from rest_framework import serializers

class CoinSerializer(serializers.ModelSerializer):
    last_price_snapshot = serializers.SerializerMethodField()

    class Meta:
        model = Coin
        fields = ["coin_id", "name", "threshold", "tolerance", "alert_above", "last_price_snapshot"]

    def get_last_price_snapshot(self, coin):
        snapshot = coin.pricesnapshot_set.order_by("-time").first()
        return snapshot.price if snapshot else None


class PriceSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSnapshot
        fields = ["price", "coin", "time", "notified"]
