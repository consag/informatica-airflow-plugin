"""
 Definition to run a test scorecard
"""

from datetime import datetime, timedelta
from airflow import DAG
from InformaticaPlugin import ExecuteScorecard

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
    'run_testscorecard',
    start_date=datetime(2019, 11, 1),
    schedule_interval=schedule_interval,
    default_args=default_args)

scorecard = ExecuteScorecard(
    task_id = "task_testscorecard",
    scorecard_path = "/SchedulerDemo/sc_SchedulerTest1",
    dag=dag
)

