from rest_framework import routers

from storage.views import LotImageViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register(r'storage/images', LotImageViewSet)
