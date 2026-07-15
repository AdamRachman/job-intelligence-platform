from src.runner.scrape_jobs import scrape_all

jobs = scrape_all(
    "Data Engineer"
)

print(len(jobs))