from .views import OfferViewSet, RFQViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'offers', OfferViewSet)
router.register(r'rfqs', RFQViewSet)

urlpatterns = router.urls