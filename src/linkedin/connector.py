from src.connector.base_connector import BaseConnector
from src.schema.job_schema import create_job
from src.linkedin.search_parser import extract_search_metadata
from src.linkedin.detail_parser import extract_detail_metadata

class LinkedInConnector(BaseConnector):

    BASE_URL = "https://www.linkedin.com"

    SEARCH_ENDPOINT = (
        "/jobs-guest/jobs/api/seeMoreJobPostings/search"
    )

    DETAIL_ENDPOINT = (
        "/jobs-guest/jobs/api/jobPosting"
    )

    def __init__(self):

        super().__init__()

    # ====================================================
    # Build Search URL
    # ====================================================

    def build_search_url(self):

        return (
            self.BASE_URL +
            self.SEARCH_ENDPOINT
        )

    # ====================================================
    # Build Search Parameters
    # ====================================================

    def build_search_params(
        self,
        keyword,
        location="Indonesia",
        start=0
    ):

        return {

            "keywords": keyword,

            "location": location,

            "start": start

        }

    # ====================================================
    # Download Search Page
    # ====================================================

    def fetch_search_page(
        self,
        keyword,
        location,
        start
    ):

        url = self.build_search_url()

        params = self.build_search_params(
            keyword,
            location,
            start
        )

        return self.fetch_page(
            url,
            params=params
        )                                                          

    # ====================================================
    # Extract Job Cards
    # ====================================================

    def extract_job_cards(self, soup):

        return soup.find_all(

            "div",

            class_="base-search-card"

        )

    # ====================================================
    # Parse Search Metadata
    # ====================================================

    def parse_search_metadata(self, job_card):

        return extract_search_metadata(job_card)

    # ====================================================
    # Download Detail Page
    # ====================================================

    def fetch_detail_page(self, job_id):

        detail_url = (
            f"{self.BASE_URL}"
            f"{self.DETAIL_ENDPOINT}"
            f"/{job_id}"
        )

        return self.fetch_page(detail_url)

    # ====================================================
    # Parse Detail Metadata
    # ====================================================

    def parse_detail_metadata(self, soup):

        return extract_detail_metadata(soup)

    # ====================================================
    # Combine Search + Detail
    # ====================================================

    def process_job(self, job_card):

        search_data = self.parse_search_metadata(
            job_card
        )

        soup = self.fetch_detail_page(
            search_data["job_id"]
        )

        detail_data = self.parse_detail_metadata(
            soup
        )

        job = create_job()

        job.update(search_data)
        job.update(detail_data)

        return job

    # ====================================================
    # Main Entry
    # ====================================================

    def scrape(

        self,

        keyword,

        location="Indonesia",

        max_results=25

    ):

        jobs = []

        start = 0

        while len(jobs) < max_results:

            print("=" * 60)
            print(f"Keyword : {keyword}")
            print(f"Start    : {start}")

            soup = self.fetch_search_page(

                keyword,

                location,

                start

            )

            cards = self.extract_job_cards(
                soup
            )

            print(f"Found {len(cards)} job cards")

            if len(cards) == 0:
                break

            for i, card in enumerate(cards, start=1):

                print(
                    f"Processing Job {start+i}"
                )

                try:

                    job = self.process_job(
                        card
                    )

                    jobs.append(job)

                except Exception as e:

                    print(e)

                if len(jobs) >= max_results:
                    break

                self.random_delay()

            start += len(cards)

        return jobs