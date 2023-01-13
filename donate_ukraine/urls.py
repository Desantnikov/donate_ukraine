from rest_framework import routers

from donate_ukraine.views import LotListRetrieveViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('lots', LotListRetrieveViewSet, basename='lots')
