from products.models import Product, PriceSnapshot
from rest_framework import permissions, viewsets

from products.serializers import PriceSnapshotSerializer, ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Products.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class PriceSnapshotViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for viewing price snapshots
    """
    queryset = PriceSnapshot.objects.all()
    serializer_class = PriceSnapshotSerializer
