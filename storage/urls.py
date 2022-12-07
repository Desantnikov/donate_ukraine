from storage.views import LotImageViewSet

from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'images', LotImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
