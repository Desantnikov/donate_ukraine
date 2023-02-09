from rest_framework import routers

from lots.views import LotListCreateRetrieveUpdateViewSet, LotListRetrieveUpdateViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('lots', LotListCreateRetrieveUpdateViewSet, basename='lots')
router.register('my-lots', LotListRetrieveUpdateViewSet, basename='lots/my')
