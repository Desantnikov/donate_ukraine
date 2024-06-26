import datetime
import logging

import requests
from rest_framework.exceptions import AuthenticationFailed, ValidationError


class MonobankApiService:
    API_URL = "https://api.monobank.ua"
    JAR_URL = "https://send.monobank.ua"
    HANDLER_URL = f"{JAR_URL}/api/handler"  # URL which returns brief jar info without api key

    def __init__(self, api_token=None):
        self.logger = logging.getLogger(__name__)

        self.api_token = api_token
        self.auth_headers = {"X-Token": self.api_token}
        self.user_info = self.fetch_user_info()

    def fetch_user_info(self):
        """
        https://api.monobank.ua/docs/#tag/Kliyentski-personalni-dani/paths/~1personal~1client-info/get
        """

        self.logger.info("Fetching user info")

        response = requests.get(
            url=f"{self.API_URL}/personal/client-info",
            headers=self.auth_headers,
        ).json()

        self.raise_errors(response)

        return response

    def fetch_jar_transactions_by_id(self, jar_id):
        current_time = datetime.datetime.now()
        period_start = current_time - datetime.timedelta(days=30)
        period_start_timestamp = int(period_start.timestamp())

        response = requests.get(
            url=f"{self.API_URL}/personal/statement/{jar_id}/{period_start_timestamp}",
            headers=self.auth_headers,
        ).json()

        self.raise_errors(response)

        return response

    def get_jar_by_send_id(self, send_id):
        jars = self.user_info["jars"]

        # `jar_data["sendId"]` returned by API looks like `jar/NCJSIWBYSHD`
        # while in `send_id` we store like `NCJSIWBYSHD`
        filtered_jar = filter(lambda jar_data: send_id in jar_data["sendId"], jars)
        jar = next(filtered_jar, None)

        if jar is None:
            raise Exception("Jar with such sendId not found in user's data")

        return jar

    def raise_errors(self, response: dict):
        if "errorDescription" not in response:
            return

        if response["errorDescription"] == "Unknown 'X-Token'":
            raise AuthenticationFailed({"api_token": "Could not authorize to monobank api with this token"})

        raise ValidationError({"monobank_api_error": response["errorDescription"]})
