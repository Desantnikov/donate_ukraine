from django.urls import path, include


LIST_VIEWSET_MAPPING = {"get": "list", "post": "create"}
DETAILS_VIEWSET_MAPPING = {"get": "retrieve", "put": "update"}


urlpatterns = [
    path('', include("donate_ukraine.urls")),
    path('storage', include("storage.urls")),
]
