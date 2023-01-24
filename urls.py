from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework.permissions import AllowAny

from lots.urls import router as lots_router
from monobank.urls import router as monobank_router
from storage.urls import router as storage_router
from users.urls import router as users_router, urlpatterns as users_urlpatterns


router = routers.DefaultRouter(trailing_slash=False)

router.registry.extend(storage_router.registry)
router.registry.extend(lots_router.registry)
router.registry.extend(monobank_router.registry)
router.registry.extend(users_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    *users_urlpatterns,  # TODO: refactor
]


if settings.DEBUG:
    schema_view = get_schema_view(
       openapi.Info(
          title="DonateUA private API",
          default_version='v1',
       ),
       public=True,
       permission_classes=[AllowAny],  # TODO: Remove schema before deploy
    )

    urlpatterns += re_path('api-schema', schema_view.with_ui('swagger', cache_timeout=0), name='schema-view'),
