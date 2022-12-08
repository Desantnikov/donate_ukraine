# from rest_framework.test import APIRequestFactory
# from django.urls import reverse
# from storage.views import LotImageViewSet
# from storage.urls import urlpatterns as storage_urlpatterns
#
# from donate_ukraine.models import User
#
#
# def test_roles_q(admin_user, admin_client_with_jwt):
#     lots_endpoint_path = reverse("lotimage-list")
#
#     view_permissions = LotImageViewSet.view_permissions
#
#     assert admin_user.role == 'admin'
#     response = admin_client_with_jwt.get(path=lots_endpoint_path)  # list
#     response = admin_client_with_jwt.post(path=lots_endpoint_path)  # create
#     response = admin_client_with_jwt.get(path=f'{lots_endpoint_path}/1')  # retrieve
#
