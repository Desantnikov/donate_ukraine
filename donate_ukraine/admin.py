from django.contrib import admin

from .models import User, Lot


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")


class LotAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "creator")


admin.site.register(User, UserAdmin)
admin.site.register(Lot, LotAdmin)
