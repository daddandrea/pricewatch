from tracker.models import Coin, PriceSnapshot
from rest_framework import serializers

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ["coin_id", "name", "threshold", "tolerance", "alert_above"]

class PriceSnapshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceSnapshot
        fields = ["price", "coin", "time"]
