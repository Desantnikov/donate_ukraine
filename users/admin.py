from django.contrib import admin
from users.models import User


from django.contrib import admin

# from posts.models import Post

from guardian.admin import GuardedModelAdmin


class MyModelAdmin(GuardedModelAdmin):
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(User, MyModelAdmin)
