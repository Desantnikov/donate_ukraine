from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

from donate_ukraine.urls import router as donate_ukraine_router
from donate_ukraine.urls import urlpatterns as donate_ukraine_urlpatterns
from storage.urls import router as storage_router
from monobank.urls import router as monobank_router

from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter(trailing_slash=False)

router.registry.extend(storage_router.registry)
router.registry.extend(donate_ukraine_router.registry)
router.registry.extend(monobank_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    *donate_ukraine_urlpatterns,  # is it ok to add VIews like that?
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
