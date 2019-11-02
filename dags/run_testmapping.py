"""
 Definition to run a test mapping
"""

from __future__ import division, absolute_import, print_function

from datetime import datetime, timedelta

from airflow import DAG

from informatica_plugin import ExecuteMapping

dag_id = "run_mapping"
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

