from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'start_date': datetime(2023, 1, 1),
}

dag = DAG('simple_dependency_example', default_args=default_args, schedule_interval='@daily')

start = DummyOperator(task_id='start', dag=dag)
extract = DummyOperator(task_id='extract', dag=dag)
transform = DummyOperator(task_id='transform', dag=dag)
load = DummyOperator(task_id='load', dag=dag)

start >> extract >> transform >> load