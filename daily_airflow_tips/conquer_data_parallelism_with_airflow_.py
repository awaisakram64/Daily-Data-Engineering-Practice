from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.subdag_operator import SubDagOperator
from datetime import datetime

def branches():
    # Example decision logic
    return 'task_2' if datetime.now().second % 2 == 0 else 'task_3'

def subdag(parent_dag_name, child_dag_name, args):
    dag_subdag = DAG(
        dag_id=f'{parent_dag_name}.{child_dag_name}',
        default_args=args,
        schedule_interval='@once',
    )

    with dag_subdag:
        start = DummyOperator(task_id='start')
        end = DummyOperator(task_id='end')
        start >> end

    return dag_subdag

args = {'start_date': datetime(2023, 10, 10)}

with DAG('parallel_processing_dag', default_args=args, schedule_interval='@daily') as dag:
    start = DummyOperator(task_id='start')

    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=branches
    )

    processing_1 = SubDagOperator(
        task_id='task_2',
        subdag=subdag('parallel_processing_dag', 'task_2', args)
    )

    processing_2 = SubDagOperator(
        task_id='task_3',
        subdag=subdag('parallel_processing_dag', 'task_3', args)
    )

    combine_results = DummyOperator(task_id='combine_results', trigger_rule='none_failed')

    start >> branching >> [processing_1, processing_2] >> combine_results