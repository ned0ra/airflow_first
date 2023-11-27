from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator

with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 9 * * *") as dag:

    first = BashOperator(task_id="first", bash_command=f"python3 /opt/airflow/dags/dag.py")

    second = BashOperator(task_id="second", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    first>>second>> airflow()