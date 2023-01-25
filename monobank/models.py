from django.utils import timezone
from django.db import models
from django.utils.timezone import now

from monobank.api_wrapper import MonobankApiWrapper


class MonobankJar(models.Model):
    title = models.CharField(max_length=40, default="")

    monobank_id = models.CharField(max_length=40, null=True)  # monobank id like `8OWpMMCU-Tfy11Nha66csZZE`
    send_id = models.TextField(max_length=40, default="")  # like "jar/7Rz7u9kkcy"

    current_balance = models.IntegerField(default=0)  # all cash countes in coins, 5000 == 50.00$
    goal = models.IntegerField(default=0)
    highest_bid = models.IntegerField(default=0)

    last_updated = models.DateTimeField(default=now)

    @property
    def link(self):
        return f"{MonobankApiWrapper.JAR_URL}/{self.send_id}"

    def update_data(self):
        api_wrapper = MonobankApiWrapper(api_token=self.lot.creator.api_token)

        jar_data = api_wrapper.get_jar_by_send_id(send_id=self.send_id)

        self.title = jar_data["title"]
        self.monobank_id = jar_data["id"]
        self.current_balance = jar_data["balance"]
        self.goal = jar_data["goal"]

        transactions = api_wrapper.fetch_jar_transactions_by_id(self.monobank_id)

        if transactions:  # be sure we are not trying to take max() of empty list (if no transactions in thhat perios)
            self.highest_bid = max([transaction["amount"] for transaction in transactions])

        self.last_updated = timezone.now()

        # self.save()
