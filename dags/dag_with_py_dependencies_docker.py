from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    'owner': 'herkoa',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


@dag(
    dag_id='create_dag_with_python_dependencies_docker_v08',
    default_args=default_args,
    description='Apache Airflow DAG with python dependencies docker',
    start_date=(datetime(2023, 7, 27)),
    schedule='0 0 * * *'
)
def run():
    @task
    def get_sklearn():
        import sklearn
        print(f'scikit-learn with version: {sklearn.__version__}')


    @task
    def get_matplotlib():
        import matplotlib
        print(f'matplotlib with version: {matplotlib.__version__}')


    get_sklearn()
    get_matplotlib()

dagger = run()


