from django.contrib import admin

from storage.models import LotImage


class LotImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(LotImage, LotImageAdmin)
