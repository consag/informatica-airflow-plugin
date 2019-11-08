"""
 Definition to run a test workflow
"""

from datetime import datetime, timedelta
from airflow import DAG
from InformaticaPlugin import ExecuteWorkflow

schedule_interval = None

default_args = {
    'owner': 'Jac. Beekers',
    'depends_on_past': False,
    'email': ['noone@nowhere.no'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=30)
}

dag = DAG(
    'run_testworkflow',
    start_date=datetime(2019, 11, 1),
    schedule_interval=schedule_interval,
    default_args=default_args)

workflow = ExecuteWorkflow(
    task_id = "task_testworkflow",
    application_name ="APP_TestScheduler",
    workflow_name = "wf_TestHumanTaskWorkflow",
    dag=dag
)

