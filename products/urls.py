from rest_framework import routers

from products.views import CoinViewSet, PriceSnapshotViewSet

router = routers.DefaultRouter()
router.register(r'coins', CoinViewSet)
router.register(r'price_snapshots', PriceSnapshotViewSet)
urlpatterns = router.urls
