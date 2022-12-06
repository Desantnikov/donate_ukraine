from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from django.contrib import admin
from django.urls import path

from donate_ukraine.views import LotViewSet, UserViewSet, UserInfoViewSet, LogoutView


LIST_VIEWSET_MAPPING = {"get": "list", "post": "create"}
DETAILS_VIEWSET_MAPPING = {"get": "retrieve", "put": "update"}


urlpatterns = [
    path("admin/", admin.site.urls),
    # send 'username' and 'password', receive 'access' and 'refresh' tokens
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("logout", LogoutView.as_view()),
    # send 'refresh', receive 'access'
    path("login/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("lots/", LotViewSet.as_view(LIST_VIEWSET_MAPPING)),
    path("lots/<int:pk>", LotViewSet.as_view(DETAILS_VIEWSET_MAPPING)),
    path("users/", UserViewSet.as_view(LIST_VIEWSET_MAPPING)),
    path("users/<int:pk>", UserViewSet.as_view(DETAILS_VIEWSET_MAPPING)),
    path("users/info", UserInfoViewSet.as_view({"get": "retrieve"})),  # get current user data
]
