from airflow.contrib.operators.gcs_list_operator import GoogleCloudStorageListOperator
from airflow.contrib.sensors.gcs_sensor import GoogleCloudStoragePrefixSensor
import datetime as dt
from airflow.models import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator

GOOGLE_CLOUD_STORAGE_CONN_ID = 'gcp_conn'
BUCKET_NAME = 'airflow-data-hea'


lasthour = dt.datetime.now() - dt.timedelta(hours=1)

args = {
    'owner': 'herkoa',
    'retries': 5,
    'start_date': lasthour,
    'depends_on_past': False
}

with DAG(
    dag_id='create_dag_with_gcp_bucket_conn_v03',
    default_args=args,
    schedule_interval=None
) as dag:
    # GCS_File_list = GoogleCloudStorageListOperator(
    #     task_id='list_Files',
    #     bucket=BUCKET_NAME,
    #     prefix='data/product-delivery.csv',
    #     delimiter='.csv',
    #     google_cloud_storage_conn_id=GOOGLE_CLOUD_STORAGE_CONN_ID,
    #     dag=dag
    # )
    file_sensor = GoogleCloudStoragePrefixSensor(
        task_id='gcs_polling',
        bucket=BUCKET_NAME,
        google_cloud_conn_id=GOOGLE_CLOUD_STORAGE_CONN_ID,
        prefix='data/product-delivery.csv',
        dag=dag
    )
    trigger = TriggerDagRunOperator(
        task_id='trigger_dag_{timestamp}_rerun'.format(
            timestamp=((dt.datetime.now() - dt.datetime.utcfromtimestamp(0)).total_seconds() * 1000)),
        trigger_dag_id="GCS_sensor_dag",
        dag=dag
    )

# file_sensor >> GCS_File_list >> trigger
file_sensor >> trigger
