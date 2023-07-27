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

## Additional notes on scripts
[dag_with_postgres_operator.py](dags%2Fdag_with_postgres_operator.py)
- after adding ports: -5432:5432 and hostname: postgres (or use host.docker.internal instead), in docker-compose.yaml, rebuild postgress service:  docker compose up -d --no-deps --build postgres
- create connection to postgres db

[dag_with_py_dependencies_docker.py](dags%2Fdag_with_py_dependencies_docker.py)
- after building a custom image:  docker build . --tag hea_airflow-with-docker:latest
- rebuild webserver and scheduler containers:  docker compose up -d --no-deps --build airflow-webserver airflow-scheduler




