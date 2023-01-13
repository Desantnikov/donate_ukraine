from rest_framework import routers

from lots.views import LotListCreateRetrieveViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('lots', LotListCreateRetrieveViewSet, basename='lots')
