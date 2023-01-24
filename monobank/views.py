from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import GenericViewSet

from mixins.views import ListModelMixin, RetrieveModelMixin
from monobank.models import MonobankJar
from monobank.serializers import MonobankJarSerializer


# TODO: Remove this view
class MonobankJarViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = [IsAdminUser]

    queryset = MonobankJar.objects.all()
    serializer_class = MonobankJarSerializer
