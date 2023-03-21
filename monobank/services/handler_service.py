import datetime
import logging

import requests
from rest_framework.exceptions import AuthenticationFailed, ValidationError


class MonobankHandlerService:
    API_URL = "https://api.monobank.ua"
    JAR_URL = "https://send.monobank.ua"
    HANDLER_URL = f"{JAR_URL}/api/handler"  # URL which returns brief jar info without api key

    def __init__(self, api_token=None):
        self.logger = logging.getLogger(__name__)

    def fetch_user_info(self):
        return {}

    def fetch_jar_transactions_by_id(self, jar_id):
        return {}

    def get_jar_by_send_id(self, send_id):
        payload = {
            "c": "hello",  # action name
            "clientId": send_id.strip("jar/"),  # stored jar/KJASDJNAS, have to take only KJASDJNAS
            "Pc": "sample",  # could be any non-blank
        }
        raw_response = requests.post(url=self.HANDLER_URL, json=payload).json()

        response = {}
        response["title"] = raw_response["name"]
        response["id"] = None  # no id in response
        response["balance"] = raw_response["jarAmount"]
        response["goal"] = raw_response["jarGoal"]

        return response

    def raise_errors(self, response: dict):
        if "errorDescription" not in response:
            return

        if response["errorDescription"] == "Unknown 'X-Token'":
            raise AuthenticationFailed({"api_token": "Could not authorize to monobank api with this token"})

        raise ValidationError({"monobank_api_error": response["errorDescription"]})
