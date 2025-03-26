from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def push_xcom(**context):
    # Push a message to XCom
    context['ti'].xcom_push(key='message', value='Hello from task 1!')

def pull_xcom(**context):
    # Pull the message from XCom
    message = context['ti'].xcom_pull(key='message', task_ids='task1')
    print(f'Received message: {message}')

default_args = {
    'start_date': datetime(2023, 10, 5),
    'catchup': False,
}

dag = DAG('xcom_example', default_args=default_args, schedule_interval='@once')

task1 = PythonOperator(
    task_id='task1',
    python_callable=push_xcom,
    provide_context=True,
    dag=dag
)

task2 = PythonOperator(
    task_id='task2',
    python_callable=pull_xcom,
    provide_context=True,
    dag=dag
)

task1 >> task2