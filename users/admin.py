from django.contrib import admin

from users.models import User


class MyModelAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(User, MyModelAdmin)
