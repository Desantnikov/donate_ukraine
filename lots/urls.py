from rest_framework import routers

from lots.views import LotListCreateRetrieveUpdateViewSet, MyLotsListRetrieveUpdateViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('lots', LotListCreateRetrieveUpdateViewSet, basename='lots')
router.register('my-lots', MyLotsListRetrieveUpdateViewSet, basename='lots/my')
