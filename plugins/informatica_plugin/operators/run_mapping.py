import time
import random

from airflow import models
from airflow import utils as airflow_utils

from devops-informatica-tools import

class RunMapping(models.BaseOperator):
    @airflow_utils.apply_defaults
    def __init__(self, **kwargs):
        super(RunMapping, self).__init__(
            **kwargs)

    def execute(self, context):
        waiting_time = 2 + random.random() * 2
        time.sleep(waiting_time)
        print("dag: " + self.dag.full_filepath)
        print("dag_id: " + self.dag_id)
        print("task_type: " + self.task_type)
        