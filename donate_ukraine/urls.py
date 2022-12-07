from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.contrib import admin
from django.urls import path

from donate_ukraine.views import LotViewSet, UserViewSet, UserInfoViewSet, LogoutViewSet


LIST_VIEWSET_MAPPING = {"get": "list", "post": "create"}
DETAILS_VIEWSET_MAPPING = {"get": "retrieve", "put": "update"}


urlpatterns = [
    path("admin", admin.site.urls),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout", LogoutViewSet.as_view({"post": "post"})),
    path("users/info", UserInfoViewSet.as_view({"get": "retrieve"})),
    path("lots/", LotViewSet.as_view(LIST_VIEWSET_MAPPING)),
    path("lots/<int:pk>", LotViewSet.as_view(DETAILS_VIEWSET_MAPPING)),
    path("users", UserViewSet.as_view(LIST_VIEWSET_MAPPING)),
    path("users/<int:pk>", UserViewSet.as_view(DETAILS_VIEWSET_MAPPING)),
]
