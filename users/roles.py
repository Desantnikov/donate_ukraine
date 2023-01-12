from rest_framework_roles.roles import is_admin, is_user


def is_auctioneer(request, view):
    return is_user(request, view) and request.user.role == "auctioneer"


ROLES = {
    "admin": is_admin,
    "user": is_user,
    "auctioneer": is_auctioneer,
}
