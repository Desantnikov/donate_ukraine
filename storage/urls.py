from django.urls import include, path
from rest_framework import routers

from storage.views import LotImageViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'images', LotImageViewSet)

urlpatterns = [
    path('/', include(router.urls)),  # TODO: Remove slash
]
