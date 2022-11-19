from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.routers import DefaultRouter
from donate_ukraine.serializers import LotSerializer


from donate_ukraine.models import Lot


class LotList(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        # lots = Lot.objects.all()
        # lots = Lot.objects.all()
        # lots = Lot.objects.all()
        # serializer = LotSerializer(lots, many=True)
        # return Response(serializer.data)
        return Response(
            {
                'creator': 'ochko',
                'description': 'description',
                'photos': 'fuck you',
                'requisites': 'and fuck you one more time',
                'report_text': 'and again',
                'report_images': 'fuck off'
            }
        )