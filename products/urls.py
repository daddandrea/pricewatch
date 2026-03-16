from rest_framework import routers

from products.views import PriceSnapshotViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'price_snapshots', PriceSnapshotViewSet)
urlpatterns = router.urls
