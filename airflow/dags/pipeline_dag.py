from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="news_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule_interval="@hourly",
    catchup=False
) as dag:

    scrape_task = BashOperator(
        task_id="scrape_news",
        bash_command="python scraper/scraper.py"
    )

    silver_task = BashOperator(
        task_id="silver_processing",
        bash_command="python spark/bronze_to_silver.py"
    )

    gold_task = BashOperator(
        task_id="gold_processing",
        bash_command="python spark/silver_to_gold.py"
    )

    scrape_task >> silver_task >> gold_task