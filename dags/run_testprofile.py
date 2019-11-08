"""
 Definition to run a test profile
"""

from datetime import datetime, timedelta
from airflow import DAG
from InformaticaPlugin import ExecuteProfile

dag_id = "run_profile"
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
    'run_testprofile',
    start_date=datetime(2019, 11, 7),
    schedule_interval=schedule_interval,
    default_args=default_args)

mapping = ExecuteProfile(
    task_id = "task_testprofile",
    profile_path = "/SchedulerDemo/Profile_SchedulerTest1",
    dag=dag
)

