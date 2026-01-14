import allure
import requests
from config.config import Configs


class EmploymentStatusAPI:
    session = requests.Session()

    @classmethod
    def get_all_employment_statuses(cls):
        """Fetch all employment statuses"""
        response = cls.session.get(Configs.EMPLOYMENT_STATUS_POSTURL, headers=Configs.HEADERS)
        if response.status_code != 200:
            allure.attach(
                response.text,
                f"GET Employment Statuses Failed ({response.status_code})",
                allure.attachment_type.TEXT
            )
            raise AssertionError(
                f"GET employment statuses failed with {response.status_code}"
            )
        # response.raise_for_status()
        return [status["name"] for status in response.json().get("data", [])]

    @classmethod
    def add_employment_status(cls, name="TestAuto78"):
        """Add a new employment status"""
        payload = {"name": name}

        response = cls.session.post(
            Configs.EMPLOYMENT_STATUS_POSTURL,
            headers=Configs.HEADERS,
            json=payload
        )
        if response.status_code not in (200, 201):
            allure.attach(
                response.text,
                f"POST Employment Status Failed ({response.status_code})",
                allure.attachment_type.TEXT
            )
            raise AssertionError(
                f"POST employment status failed with {response.status_code}: {response.text}"
            )
        # response.raise_for_status()
        return response.json()["data"]["name"]
