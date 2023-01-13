from rest_framework import routers

from lots.views import LotListCreateRetrieveUpdateViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('lots', LotListCreateRetrieveUpdateViewSet, basename='lots')
