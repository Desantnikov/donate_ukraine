from django.contrib import admin

from users.models import User


@admin.register(User)
class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ("deleted_at", "last_login")
    filter_horizontal = ("groups", "user_permissions")

    def get_queryset(self, request):
        return User.objects.with_deleted()
