"""
 Definition to run a test mapping
"""

from datetime import datetime, timedelta
from airflow import DAG
from InformaticaPlugin import ExecuteMapping

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
    'run_testmapping',
    start_date=datetime(2019, 11, 1),
    schedule_interval=schedule_interval,
    default_args=default_args)

mapping = ExecuteMapping(
    task_id = "task_testmapping",
    application_name ="APP_TestScheduler",
    mapping_name = "m_SchedulerTest1",
    dag=dag
)

