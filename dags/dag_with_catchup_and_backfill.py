from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'herkoa',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
        dag_id='create_dag_with_catchup_and_backfill_v5',
        default_args=default_args,
        description='Apache Airflow DAG with catchup and backfill',
        start_date=(datetime(2023, 7, 27)),
        schedule='@daily',
        catchup=False
) as (dag):
    task1 = BashOperator(
        task_id="t1",
        bash_command='echo yahoo.com'
    )

"""
Given today's date datetime(2023, 7, 26) run backfill from 2023/7/1 until 2023/7/8
inside airflow-scheduler docker container enter: 
airflow dags backfill -s 2023-06-30 -e 2023-07-07 create_dag_with_catchup_and_backfill_v5
"""