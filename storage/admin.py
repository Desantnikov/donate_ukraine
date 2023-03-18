from django.contrib import admin

from storage.models import LotImage


@admin.register(LotImage)
class LotImageAdmin(admin.ModelAdmin):
    list_display = ("id", "corresponging_lot_name", "corresponging_lot_status", "lot_id")

    def corresponging_lot_name(self, instance):
        return instance.lot_id.name

    def corresponging_lot_status(self, instance):
        return instance.lot_id.status
