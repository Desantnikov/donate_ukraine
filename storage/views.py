from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from mixins.views import AllActionsMixin
from storage.models import LotImage
from storage.serializers import ImageSerializer


class LotImageViewSet(GenericViewSet, AllActionsMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = ImageSerializer
    queryset = LotImage.objects.all()
