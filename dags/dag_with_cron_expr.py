# cron online: https://crontab.guru/
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'herkoa',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
        dag_id='create_dag_with_cron_v2',
        default_args=default_args,
        description='Apache Airflow DAG with cron',
        start_date=(datetime(2023, 7, 11)),
        schedule='0 3 * * Tue-Fri'
) as dag:
    task1 = BashOperator(
        task_id="t1",
        bash_command='echo cron expression'
    )

    task1


