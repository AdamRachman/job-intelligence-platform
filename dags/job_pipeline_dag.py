from airflow import DAG

from airflow.operators.python import PythonOperator

from datetime import datetime


from src.runner.scrape_jobs import main as scrape_jobs
from src.bronze.bronze_loader import main as bronze_loader
from src.silver.silver_loader import main as silver_loader
from src.gold.gold_loader import main as gold_loader

from src.sync.gold_to_sheet_sync import sync_gold_to_sheet



default_args = {
    "owner": "adam",
    "retries": 1,
}

def send_ntfy_notification(**context):

    ti = context["ti"]

    jobs = ti.xcom_pull(
        task_ids="gold_enrichment"
    )


    if not jobs:

        print(
            "No new jobs for notification."
        )

        return


    from src.notification.service import (
        send_job_notifications
    )

    print(
        f"Jobs received from Gold: {len(jobs)}"
    )

    send_job_notifications(
        jobs
    )


with DAG(
    dag_id="job_intelligence_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 7, 24),
    schedule="0 8,16 * * *",
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
        show_return_value_in_logs=False,
    )


    sync_sheet_task = PythonOperator(
        task_id="sync_google_sheet",
        python_callable=sync_gold_to_sheet,
    )

    ntfy_task = PythonOperator(
        task_id="send_ntfy_notification",
        python_callable=send_ntfy_notification,
    )

    scrape_task >> bronze_task >> silver_task >> gold_task
    gold_task >> sync_sheet_task
    gold_task >> ntfy_task