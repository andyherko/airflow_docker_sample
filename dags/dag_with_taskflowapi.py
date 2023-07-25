from datetime import datetime, timedelta
from airflow.decorators import dag, task

default_args = {
    'owner': 'herkoa',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


@dag(
    dag_id='create_dag_with_taskflow_api_v4',
    default_args=default_args,
    description='Apache Airflow DAG with taskflow api',
    start_date=datetime(2023, 7, 25),
    schedule='@daily')
def greeting_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Dan',
            'last_name': 'Peeks'
        }

    @task
    def get_age():
        return 59

    @task
    def greet(first_name, last_name, age):
        print(f"Hi, my name is {first_name} {last_name}, "
              f"and i am {age} years old!")

    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'],
          age=age)


greet_dag = greeting_etl()
