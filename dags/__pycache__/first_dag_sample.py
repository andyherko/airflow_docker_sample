from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'herkoa', 
    'retries':5, 
    'retry_delay':timedelta(minutes=2)
 }

with DAG(
    dag_id='first_dag_sample_v3',
    description='This is first apache airflow DAG sample',
    start_date=(datetime(2023, 7, 25, 6)),
    schedule='@daily'
) as (dag):
    task1 = BashOperator(
        task_id='t1',
        bash_command='echo running task1...'
    )    
    task2 = BashOperator(
        task_id='t2',
        bash_command='echo running task2...'
    )
    task3 = BashOperator(
        task_id='t3',
        bash_command='echo running task3...')
    
    # Diff dependency methods
    task1.set_downstream(task2)
    task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    # task1 >> [task2, task3]