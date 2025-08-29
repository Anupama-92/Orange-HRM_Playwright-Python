import requests
from config.config import Configs


class EmploymentStatusAPI:
    session = requests.Session()

    @classmethod
    def get_all_employment_statuses(cls):
        """Fetch all employment statuses"""
        response = cls.session.get(Configs.EMPLOYMENT_STATUS_POSTURL, headers=Configs.HEADERS)
        response.raise_for_status()
        return [status["name"] for status in response.json().get("data", [])]

    @classmethod
    def add_employment_status(cls, name="TestAuto13"):
        """Add a new employment status"""
        payload = {"name": name}

        response = cls.session.post(
            Configs.EMPLOYMENT_STATUS_POSTURL,
            headers=Configs.HEADERS,
            json=payload
        )
        response.raise_for_status()
        return response.json()["data"]["name"]
