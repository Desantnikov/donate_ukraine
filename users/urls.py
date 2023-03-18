from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import LogoutAPIView, RestorePasswordAPIView, UserViewSet


router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),

    path("login", TokenObtainPairView.as_view(), name="login"),
    path("logout", LogoutAPIView.as_view(), name="logout"),
    path("login/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("login/restore", RestorePasswordAPIView.as_view(), name="restore")
]
