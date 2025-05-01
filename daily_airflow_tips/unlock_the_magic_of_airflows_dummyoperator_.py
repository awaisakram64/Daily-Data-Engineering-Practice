from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def my_task(*args):
    print('Task successfully executed! 🎉')

with DAG('dummy_operator_example', start_date=datetime(2023, 10, 1), schedule_interval='@daily', catchup=False) as dag:
    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')
    run_task = PythonOperator(
        task_id='run_python_task',
        python_callable=my_task
    )

    start >> run_task >> end