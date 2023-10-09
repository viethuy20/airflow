from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
default_args={
    "owner":"huy",
    "retries":5,
    "retry_delay" : timedelta(minutes=2)
}
with DAG(
    dag_id = "first1_dag",
    default_args = default_args,
    description="this is our first dag",
    start_date=datetime(2023,9,19,2),
    schedule_interval="@daily"
 ) as dag:
    task1 = BashOperator(
        task_id = "second_task",
        bash_command="echo hello work, this is first time"
    )
    task1