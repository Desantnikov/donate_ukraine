from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from donate_ukraine.mixins.views import ListModelMixin, RetrieveModelMixin


from monobank.models import MonobankJar
from monobank.serializers import MonobankJarSerializer


class MonobankJarViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = MonobankJar.objects.all()
    serializer_class = MonobankJarSerializer
