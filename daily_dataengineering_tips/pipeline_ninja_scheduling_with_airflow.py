from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

# Define a simple DAG (Directed Acyclic Graph)
define_dag = DAG(
    'simple_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval='@daily'
)

# Define tasks
task1 = DummyOperator(
    task_id='start',
    dag=define_dag
)

task2 = DummyOperator(
    task_id='end',
    dag=define_dag
)

# Set task dependencies
task1 >> task2