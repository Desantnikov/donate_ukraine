from django.contrib import admin

from users.models import User


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ("deleted_at",)
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(User, MyModelAdmin)
