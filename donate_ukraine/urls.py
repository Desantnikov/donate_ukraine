from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path

from donate_ukraine.instances import LotViewSet, UserViewSet


LIST_VIEWSET_MAPPING = {"get": "list", "post": "create"}
DETAILS_VIEWSET_MAPPING = {"get": "retrieve", "put": "update"}


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register", RegisterView.as_view()),
    path("login", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("lots/", LotViewSet.as_view(LIST_VIEWSET_MAPPING)),
    path("lots/<int:pk>", LotViewSet.as_view(DETAILS_VIEWSET_MAPPING)),
    path("users/", UserViewSet.as_view(LIST_VIEWSET_MAPPING)),
    path("users/<int:pk>", UserViewSet.as_view(DETAILS_VIEWSET_MAPPING)),
]
