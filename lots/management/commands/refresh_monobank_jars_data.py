import time

from django.core.management.base import BaseCommand

from lots.models import Lot


class Command(BaseCommand):
    help = "Updates monobank jar data for all active and non undermoderation lots"

    def add_arguments(self, parser):
        parser.add_argument("--filter_by_is_active", default=True, help="Update deactivated lots also")
        parser.add_argument("--filter_by_is_under_moderation", default=True, help="Update under moderation lots also")
        parser.add_argument("--all", default=True, help="Update all lots")
        parser.add_argument("--delay", default=30, help="Delay between update requests")

    def handle(self, *args, **options):
        update_all = options["all"]
        filter_by_is_active = options["filter_by_is_active"] or update_all
        filter_by_is_under_moderation = options["filter_by_is_under_moderation"] or update_all

        lots_to_update = Lot.objects.all()
        if filter_by_is_active and not update_all:
            lots_to_update.exclude(is_active=False)
        if filter_by_is_under_moderation and not update_all:
            lots_to_update.exclude(is_under_moderation=False)

        errors = []
        for lot in Lot.objects.all():
            try:
                time.sleep(options["delay"])
                lot.monobank_jar.update_data()
            except Exception as e:
                errors.append(e)

        for exception in errors:
            print(f"Error: {exception.args}\r\n")
