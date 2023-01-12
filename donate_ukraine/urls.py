from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from donate_ukraine.views import LogoutViewSet, LotViewSet, UserViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('users', UserViewSet, basename='users')
router.register('lots', LotViewSet, basename='lots')
router.register('logout', LogoutViewSet, basename='logout')


urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="login-list"),  # '-list' to be consistent with ViewSets paths
    path("login/refresh", TokenRefreshView.as_view(), name="refresh-list"),
]
