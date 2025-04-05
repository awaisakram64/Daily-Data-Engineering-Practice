from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
def process_data(ds, **kwargs):
    print(f'Processing data for date: {ds}')
    # Your data processing logic here
with DAG(dag_id='data_processing', default_args={'owner': 'airflow', 'start_date': datetime(2023, 10, 1)}, schedule_interval='@daily') as dag:
    process_data_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
        provide_context=True
    )