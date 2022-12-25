from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from donate_ukraine.mixins.views import ListCreateRetrieveUpdateMixin
from storage.models import LotImage
from storage.serializers import ImageSerializer


class LotImageViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    permission_classes = [IsAuthenticated]

    serializer_class = ImageSerializer
    queryset = LotImage.objects.all()
