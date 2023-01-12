from rest_framework import routers

from donate_ukraine.views import LotViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('lots', LotViewSet, basename='lots')
