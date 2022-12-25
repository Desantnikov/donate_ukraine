import datetime

import requests


class MonobankApiWrapper:
    API_URL = "https://api.monobank.ua"

    def __init__(self, api_token):
        self.api_token = api_token
        self.auth_headers = {"X-Token": self.api_token}
        print(f"\r\nTOKEN: {self.api_token}")  #
        self.user_info = self.fetch_user_info()

    def fetch_user_info(self):
        """
        https://api.monobank.ua/docs/#tag/Kliyentski-personalni-dani/paths/~1personal~1client-info/get
        """

        response = requests.get(
            url=f"{self.API_URL}/personal/client-info",
            headers=self.auth_headers,
        )

        return response.json()

    def fetch_jar_transactions_by_id(self, jar_id):
        current_time = datetime.datetime.now()
        period_start = current_time - datetime.timedelta(days=30)
        period_start_timestamp = int(period_start.timestamp())

        jar_transactions = requests.get(
            url=f"{self.API_URL}/personal/statement/{jar_id}/{period_start_timestamp}",
            headers=self.auth_headers,
        ).json()

        return jar_transactions

    def get_jar_by_title(self, title):
        jars = self.user_info["jars"]

        filtered_jars = list(filter(lambda jar: jar["title"] == title, jars))

        if len(jars) > 1:
            raise Exception("User has more than one jars with such title")

        return filtered_jars[0] if filtered_jars else None
