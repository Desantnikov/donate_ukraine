from rest_framework.viewsets import GenericViewSet

from mixins.views import ListCreateRetrieveUpdateMixin
from storage.models import LotImage
from storage.serializers import ImageSerializer


class LotImageViewSet(GenericViewSet, ListCreateRetrieveUpdateMixin):
    serializer_class = ImageSerializer
    queryset = LotImage.objects.all()
