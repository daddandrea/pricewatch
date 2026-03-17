from products.models import Coin, PriceSnapshot
from rest_framework import permissions, viewsets

from products.serializers import PriceSnapshotSerializer, CoinSerializer

class CoinViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Coin.
    """
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    permission_classes = [permissions.AllowAny]

class PriceSnapshotViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing price snapshots
    """
    queryset = PriceSnapshot.objects.all()
    serializer_class = PriceSnapshotSerializer
