from rest_framework.permissions import AllowAny, BasePermission, DjangoModelPermissions


BASIC_PERMISSIONS = ("change_user",)  # granted on for any user on creation


class AllPermissionsSeparately(DjangoModelPermissions):
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


# specifically for the UserViewSet - anyone can register,
class AnyoneCanCreateOtherDepends(AllPermissionsSeparately):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True

        return super(AnyoneCanCreateOtherDepends, self).has_permission(request, view)
