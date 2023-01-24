from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import LogoutView, UserViewSet


router = routers.DefaultRouter(trailing_slash=False)

router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("login/refresh", TokenRefreshView.as_view(), name="refresh"),
]
