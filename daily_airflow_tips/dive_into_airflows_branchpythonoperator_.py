from airflow import DAG
from airflow.operators.python import BranchPythonOperator, PythonOperator
from datetime import datetime

def choose_branch(**kwargs):
    sales = kwargs.get('sales', 0)
    if sales > 1000:
        return 'generate_report'
    else:
        return 'no_report'

with DAG(dag_id='sales_decision_dag', start_date=datetime(2023, 1, 1), schedule_interval='@daily') as dag:
    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=choose_branch,
        op_kwargs={'sales': 1200}
    )

    generate_report = PythonOperator(
        task_id='generate_report',
        python_callable=lambda: print('Report generated.')
    )

    no_report = PythonOperator(
        task_id='no_report',
        python_callable=lambda: print('No report needed.')
    )

    branching >> [generate_report, no_report]