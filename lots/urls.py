from rest_framework import routers

from lots.views import LotAllActionsViewSet, MyLotsListRetrieveUpdateViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('lots', LotAllActionsViewSet, basename='lots')
router.register('my-lots', MyLotsListRetrieveUpdateViewSet, basename='lots/my')
