from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from donate_ukraine.views import LogoutViewSet, LotViewSet, UserInfoViewSet, UserViewSet


LIST_VIEWSET_MAPPING = {"get": "list", "post": "create"}
DETAILS_VIEWSET_MAPPING = {"get": "retrieve", "put": "update"}


urlpatterns = [
    path("admin", admin.site.urls),

    path("login", TokenObtainPairView.as_view(), name="login"),
    path("login/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("logout", LogoutViewSet.as_view({"post": "post"}), name="logout"),

    path("users", UserViewSet.as_view(LIST_VIEWSET_MAPPING)),
    path("users/<int:pk>", UserViewSet.as_view(DETAILS_VIEWSET_MAPPING)),
    path("users/info", UserInfoViewSet.as_view({"get": "retrieve"})),

    path("lots", LotViewSet.as_view(LIST_VIEWSET_MAPPING)),
    path("lots/<int:pk>", LotViewSet.as_view(DETAILS_VIEWSET_MAPPING)),
]
