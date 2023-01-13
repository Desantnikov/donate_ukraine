from rest_framework import routers

from donate_ukraine.views import LotListCreateRetrieveViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('lots', LotListCreateRetrieveViewSet, basename='lots')
