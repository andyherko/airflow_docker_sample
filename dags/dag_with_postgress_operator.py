from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'herkoa',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
        dag_id='create_dag_with_postgres_connection_v03',
        default_args=default_args,
        description='Apache Airflow DAG with postgres connection',
        start_date=(datetime(2023, 7, 26)),
        schedule='0 0 * * *'
) as dag:
    task1 = PostgresOperator(
        task_id="create_postgres_tbl",
        postgres_conn_id='postgres_localhost',
        sql="""
            create table if not exists dag_runs (
                dag_id character varying,
                ds date,
                primary key (dag_id,ds)                
            );
        """
    )
    task2 = PostgresOperator(
        task_id="insert_into_tbl",
        postgres_conn_id='postgres_localhost',
        sql="""
             insert into dag_runs(dag_id, ds) values ('{{ dag.dag_id }}', '{{ ds }}')
         """
    )
    task3 = PostgresOperator(
        task_id="delete_data_from_tbl",
        postgres_conn_id='postgres_localhost',
        sql="""
             delete from dag_runs where dag_id = '{{ dag.dag_id }}' and ds = '{{ ds }}'
         """
    )
    task1 >> task3 >> task2

