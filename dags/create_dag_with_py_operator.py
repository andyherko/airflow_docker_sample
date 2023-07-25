from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'herkoa',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"My name is {first_name} {last_name} and I am {age} years old!!")


def get_age(ti):
    ti.xcom_push(key='age', value=33)


def get_name(ti):
    ti.xcom_push(key='first_name', value='Bob')
    ti.xcom_push(key='last_name', value='Bloomberg')


with DAG(
        dag_id='create_dag_with_py_operator_v4',
        default_args=default_args,
        description='Apache Airflow DAG with python operator',
        start_date=(datetime(2023, 7, 25)),
        schedule='@daily'
) as (dag):
    task1 = PythonOperator(
        task_id="greet",
        python_callable=greet,
        # op_kwargs={'age': 27}
    )
    task2 = PythonOperator(
        task_id="get_name",
        python_callable=get_name
    )
    task3 = PythonOperator(
        task_id="get_age",
        python_callable=get_age
    )

    [task3, task2] >> task1
