Setup from 
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html#initializing-environment

### Fetching docker-compose.yaml
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.6.3/docker-compose.yaml'

### Initializing Environment
comment out anything related to CELERY, celery worker, redis and set AIRFLOW__CORE__LOAD_EXAMPLES: 'false'

mkdir -p ./dags ./logs ./plugins ./config

linux related: echo -e "AIRFLOW_UID=$(id -u)" > .env

### Initialize the database
docker compose up airflow-init -d

user: airflow pass: airflow

## Running Airflow
docker compose up -d

go2: http://localhost:8080



