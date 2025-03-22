from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

# Define some example datasets
sources = ['source_1.csv', 'source_2.csv', 'source_3.csv']

def generate_task(source):
    return DummyOperator(
        task_id=f'process_{source}',
        retries=3
    )

with DAG(
    'dynamic_task_generation_dag',
    start_date=days_ago(1),
    schedule_interval=None
) as dag:

    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')

    # Dynamically create tasks
    for source in sources:
        task = generate_task(source)
        start >> task >> end