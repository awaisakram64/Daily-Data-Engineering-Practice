from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

# Dynamic list of tasks
task_names = ['task_1', 'task_2', 'task_3']

def create_dag(dag_id, schedule, dag_number, default_args):
    def dynamic_task():
        with DAG(dag_id, default_args=default_args, schedule_interval=schedule) as dag:
            start = DummyOperator(task_id='start')

            # Dynamically create tasks
            for task in task_names:
                dummy_task = DummyOperator(task_id=task)
                start >> dummy_task

            return dag
    return dynamic_task()

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

# Create a dynamic DAG
dag_id = 'dynamic_dag_example'
schedule = '@daily'

dynamic_dag = create_dag(dag_id, schedule, 1, default_args)