from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from donate_ukraine.models import Lot
from donate_ukraine.serializers import LotSerializer


class LotList(ListCreateAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer


class LotDetails(RetrieveUpdateDestroyAPIView):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
