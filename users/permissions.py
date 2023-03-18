from rest_framework.permissions import DjangoModelPermissions


BASIC_PERMISSIONS = (
    "change_user",
    "delete_user",
    "add_lot",
    "change_lot",
    "delete_lot",
    "add_lotimage",
    "change_lotimage",
    "delete_lotimage",
)  # granted to any user on creation


class SpecificPermissionForEachAction(DjangoModelPermissions):
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    def has_permission(self, request, view):
        # empty list means this request type accessible for all, even non-authenticated
        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)

        if not perms:
            return True

        return super(SpecificPermissionForEachAction, self).has_permission(request, view)


# specifically for the UserViewSet - anyone can register,
class AnyoneCanCreate(SpecificPermissionForEachAction):
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": [],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }


class AnyoneCanListRetrieve(SpecificPermissionForEachAction):
    perms_map = {
        "GET": [],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }
