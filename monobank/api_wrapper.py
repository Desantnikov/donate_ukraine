import datetime
import logging

import requests
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from monobank.services import MonobankApiService, MonobankHandlerService


class MonobankApiWrapper:
    API_URL = "https://api.monobank.ua"
    JAR_URL = "https://send.monobank.ua"
    HANDLER_URL = f"{JAR_URL}/api/handler"  # URL which returns brief jar info without api key

    def __init__(self, api_token=None):
        self.logger = logging.getLogger(__name__)

        if api_token:
            self.service = MonobankApiService(api_token=api_token)
            self.reserve_service = MonobankHandlerService()
            return

        self.service = MonobankHandlerService()
        self.reserve_service = None

    @property
    def reserve_service_present(self):
        return self.reserve_service is not None

    def fetch_user_info(self):
        return self.service.fetch_user_info()

    def fetch_jar_transactions_by_id(self, jar_id):
        return self.service.fetch_jar_transactions_by_id(jar_id)

    def get_jar_by_send_id(self, send_id):
        try:
            return self.service.get_jar_by_send_id(send_id)
        except Exception as e:
            self.logger.exception(f"Main monobank service failed with exception, trying reserve service", exc_info=e)
            if self.reserve_service_present:
                return self.reserve_service.get_jar_by_send_id(send_id)
