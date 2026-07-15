from src.schema.job_schema import create_job
from src.jobstreet.search_parser import extract_search_metadata
from src.jobstreet.detail_parser import extract_detail_metadata
from src.connector.base_connector import BaseConnector

class JobStreetConnector(BaseConnector):

    BASE_URL = "https://id.jobstreet.com"

    def __init__(self):

        super().__init__()

    # ====================================================
    # Build Search URL
    # ====================================================

    def build_search_url(self, keyword):

        keyword = keyword.lower().strip()

        slug = keyword.replace(" ", "-")

        return (
            f"{self.BASE_URL}/id/"
            f"{slug}-jobs"
        )

    # ====================================================
    # Build Page URL
    # ====================================================

    def build_page_url(
        self,
        search_url,
        page,
        sort_mode="ListedDate"
    ):

        params = []

        if page > 1:
            params.append(f"page={page}")

        if sort_mode is not None:
            params.append(f"sortmode={sort_mode}")

        if not params:
            return search_url

        return f"{search_url}?{'&'.join(params)}"

    # ====================================================
    # Download Search Page
    # ====================================================

    def fetch_search_page(self, page_url):

        return self.fetch_page(page_url)

    # ====================================================
    # Extract Job Cards
    # ====================================================

    def extract_job_cards(self, soup):

        return soup.find_all(
            "article",
            attrs={
                "data-testid": "job-card"
            }
        )

    # ====================================================
    # Parse Search Metadata
    # ====================================================

    def parse_search_metadata(self, job_card):

        return extract_search_metadata(job_card)

    # ====================================================
    # Download Detail Page
    # ====================================================

    def fetch_detail_page(self, detail_url):

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

        search_data = self.parse_search_metadata(job_card)

        soup = self.fetch_detail_page(
            search_data["detail_url"]
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
        max_pages=None,
        max_results=None
    ):

        search_url = self.build_search_url(keyword)

        jobs = []

        page = 1

        while True:

            if max_pages is not None and page > max_pages:
                break

            page_url = self.build_page_url(
                search_url,
                page
            )

            print("=" * 60)
            print(f"KEYWORD : {keyword}")
            print(f"PAGE    : {page}")
            print(page_url)

            soup = self.fetch_search_page(page_url)

            cards = self.extract_job_cards(soup)

            print(f"Found {len(cards)} job cards")

            if len(cards) == 0:

                print("No more job cards.")

                break

            for i, card in enumerate(cards, start=1):

                print(f"Processing Job {i} (Page {page})")

                try:

                    job = self.process_job(card)

                    jobs.append(job)
                    if (
                        max_results is not None
                        and len(jobs) >= max_results
                    ):
                        return jobs

                except Exception as e:

                    print(f"Failed Job {i} (Page {page})")
                    print(e)

                self.random_delay()

            page += 1

        return jobs