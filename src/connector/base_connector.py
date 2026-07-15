from bs4 import BeautifulSoup
import random
import time
import requests


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


class BaseConnector:

    def __init__(self):

        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    # ====================================================
    # Fetch HTML Page
    # ====================================================

    def fetch_page(
        self,
        url,
        params=None
    ):

        response = self.session.get(
            url,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return BeautifulSoup(
            response.text,
            "html.parser"
        )

    # ====================================================
    # Random Delay
    # ====================================================

    def random_delay(self):

        time.sleep(
            random.uniform(1.5, 3.0)
        )