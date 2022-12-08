from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path


LIST_VIEWSET_MAPPING = {"get": "list", "post": "create"}
DETAILS_VIEWSET_MAPPING = {"get": "retrieve", "put": "update"}


urlpatterns = [
    path('', include("donate_ukraine.urls")),
    path('storage', include("storage.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
