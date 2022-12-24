import requests


class MonobankApiWrapper:
    API_URL = "https://api.monobank.ua"

    def __init__(self, api_token):
        self.api_token = api_token
        self.auth_headers = {"X-Token": self.api_token}

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

    def fetch_jar_info_by_id(self, jar_id):
        jar_info = requests.get(
            url=f"{self.API_URL}/personal/statement/{jar_id}",
            headers=self.auth_headers,
        ).json()

        return jar_info

    def get_jar_by_title(self, title):
        jars = self.user_info["jars"]

        filtered_jars = list(filter(lambda jar: jar["title"] == title, jars))

        if len(jars) > 1:
            raise Exception("User has more than one jars with such title")

        return filtered_jars[0] if filtered_jars else None
