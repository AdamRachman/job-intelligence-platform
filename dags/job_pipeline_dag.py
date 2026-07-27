from airflow import DAG

from airflow.operators.python import PythonOperator

from datetime import datetime


from src.runner.scrape_jobs import main as scrape_jobs
from src.bronze.bronze_loader import main as bronze_loader
from src.silver.silver_loader import main as silver_loader
from src.gold.gold_loader import main as gold_loader



default_args = {
    "owner": "adam",
    "retries": 1,
}


with DAG(
    dag_id="job_intelligence_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 7, 24),
    schedule="0 1,9,17 * * *",
    catchup=False,
) as dag:


    scrape_task = PythonOperator(
        task_id="scrape_jobs",
        python_callable=scrape_jobs,
    )


    bronze_task = PythonOperator(
        task_id="bronze_ingestion",
        python_callable=bronze_loader,
    )


    silver_task = PythonOperator(
        task_id="silver_transformation",
        python_callable=silver_loader,
    )


    gold_task = PythonOperator(
        task_id="gold_enrichment",
        python_callable=gold_loader,
    )


    scrape_task >> bronze_task >> silver_task >> gold_task