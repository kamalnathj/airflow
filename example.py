import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id = "ExampleDag",
        default_args={
            "retries": 2,
            },
        start_date=datetime.datetime(2023, 1, 15),
) as dag:
        start = EmptyOperator(
                task_id="Start",
        )