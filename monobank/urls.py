from rest_framework import routers

from monobank.views import MonobankJarViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('jar', MonobankJarViewSet, basename='jars')
