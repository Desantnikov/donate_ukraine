import datetime

from django.db import models
from django.utils.timezone import now

from monobank.api_wrapper import MonobankApiWrapper


class MonobankJar(models.Model):
    # lot = models.ForeignKey(Lot, on_delete=models.CASCADE)

    title = models.CharField(max_length=40, default="")

    monobank_id = models.CharField(max_length=40, null=True)  # monobank id like `8OWpMMCU-Tfy11Nha66csZZE`
    link = models.URLField(max_length=40, default="")

    current_balance = models.IntegerField(default=0)
    goal = models.IntegerField(default=0)
    highest_bid = models.IntegerField(default=0)

    last_updated = models.DateTimeField(default=now)

    def update_data(self):
        api_wrapper = MonobankApiWrapper(api_token=self.lot.creator.api_token)

        jar_data = api_wrapper.get_jar_by_title(title=self.title)

        self.monobank_id = jar_data["id"]
        self.current_balance = jar_data["balance"]
        self.goal = jar_data["goal"]

        transactions = api_wrapper.fetch_jar_transactions_by_id(self.monobank_id)

        if transactions:  # be sure we are not trying to take max() of empty list (if no transactions in thhat perios)
            self.highest_bid = max([transaction["amount"] for transaction in transactions])

        self.last_updated = datetime.datetime.now()

        self.save()
