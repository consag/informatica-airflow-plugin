from airflow import models
from airflow import utils as airflow_utils

from execution import runMapping


class ExecuteMapping(models.BaseOperator):
    @airflow_utils.apply_defaults
    def __init__(self, **kwargs):
        super(ExecuteMapping, self).__init__(
            **kwargs)

    def execute(self, context):
        print("dag: " + self.dag.full_filepath)
        print("dag_id: " + self.dag_id)
        print("task_type: " + self.task_type)
        run_mapping = runMapping
        run_mapping.runit()
