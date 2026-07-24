from src.ai.enrich import enrich_job


response = enrich_job(

    title="Data Engineer",

    description="""
We are looking for a Data Engineer.

Requirements:

- Python
- SQL
- Apache Airflow
- Docker
- PostgreSQL

Experience 3 years.
"""
)

print(response)