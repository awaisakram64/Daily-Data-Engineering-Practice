from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.macros import ds_add
from datetime import datetime

def print_execution_date(execution_date):
    return f"Execution date is: {execution_date}"

with DAG(dag_id='macro_example_dag', 
         start_date=datetime(2023, 10, 1), 
         schedule_interval='@daily') as dag:

    task = PythonOperator(
        task_id='print_dates',
        python_callable=print_execution_date,
        op_kwargs={'execution_date': '{{ execution_date }}'}
    )

    task
