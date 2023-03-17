from django.contrib import admin

from lots.models import Lot


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ("name", "creator", "status", "created_at")
    fields = ("creator", "name", "description", "ending_date", "monobank_jar", "status", "created_at", "deleted_at")
    readonly_fields = ("created_at", "deleted_at")

    def get_queryset(self, request):
        return Lot.objects.all()
