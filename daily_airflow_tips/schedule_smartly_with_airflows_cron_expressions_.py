from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
}

dag = DAG(
    'cron_example',
    default_args=default_args,
    description='A simple cron-based DAG',
    schedule_interval='0 6 * * 1',  # At 06:00 on Monday
    start_date=datetime(2023, 10, 1),
    catchup=False,
)

dummy_task = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)
