"""
# Movie Pipeline
This pipeline will load movie associated metadata into the database.

"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from movies.movie_pipeline import movie_pipeline


default_args = {
    "owner": "Tyson",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    "movie_dag",
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 3, 7),
    catchup=False,
    tags=["movies"],
) as dag:

    grab_data = PythonOperator(
        task_id="extract_movie_titles",
        python_callable=movie_pipeline,
        op_kwargs={"titles_list": ["Naruto", "Bleach"]},
    )
