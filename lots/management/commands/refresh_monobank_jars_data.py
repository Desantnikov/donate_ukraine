import time

from django.core.management.base import BaseCommand

from lots.constants import LOT_STATUS
from lots.models import Lot


class Command(BaseCommand):
    help = "Updates monobank jar data for all active and non undermoderation lots; Only active lots by default"

    def add_arguments(self, parser):
        parser.add_argument("--update-closed", default=False, help="Update closed lots also")
        parser.add_argument("--update-under-moderation", default=True, help="Update under moderation lots also")
        parser.add_argument("--delay", default=30, help="Delay between update requests")

    def handle(self, *args, **options):
        delay = int(options["delay"])

        update_closed = options["update_closed"]
        update_under_moderation = options["update_under_moderation"]

        lots_to_update = Lot.objects.all()

        if not update_closed:
            lots_to_update = lots_to_update.exclude(status=LOT_STATUS.CLOSED)

        if not update_under_moderation:
            lots_to_update = lots_to_update.exclude(status=LOT_STATUS.MODERATION)

        self.update_lots(lots_to_update, delay=delay)

    @staticmethod
    def update_lots(lots_to_update, delay):
        errors = []
        for lot in lots_to_update:
            try:
                print(f"Updating lot: {lot}")
                time.sleep(delay)
                lot.monobank_jar.update_data()
            except Exception as e:
                errors.append(e)

        for exception in errors:
            print(f"Error: {exception.args}\r\n")  # TODO: Log
