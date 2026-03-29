from tracker.models import Coin, PriceSnapshot
from rest_framework import permissions, viewsets

from tracker.serializers import PriceSnapshotSerializer, CoinSerializer

class CoinViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Coin.
    """
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "coin_id"

class PriceSnapshotViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing price snapshots
    """
    queryset = PriceSnapshot.objects.all()
    serializer_class = PriceSnapshotSerializer

    def get_queryset(self):
        queryset = PriceSnapshot.objects.all()
        coin_id  = self.request.query_params.get("coin_id")
        if coin_id:
            queryset = queryset.filter(coin__coin_id=coin_id)
        return queryset
