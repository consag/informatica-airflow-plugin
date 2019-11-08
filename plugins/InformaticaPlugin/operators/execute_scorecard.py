from airflow.models import BaseOperator
from airflow import utils as airflow_utils, AirflowException

from execution import runScorecard

class ExecuteScorecard(BaseOperator):

    @airflow_utils.apply_defaults
    def __init__(self, scorecard_path, **kwargs):
        self.scorecard_path = scorecard_path
        super(ExecuteScorecard, self).__init__(
            **kwargs)

    def execute(self, context):
        print("dag: " + self.dag.full_filepath)
        print("dag_id: " + self.dag_id)
        print("task_type: " + self.task_type)
        print("task id: " + self.task_id)
        print("scorecard_path: " + self.scorecard_path)
        arguments = [
            "-s",
            self.scorecard_path,
            # TODO: the others to be added
        ]
        infa = runScorecard.ExecuteInformaticaProfile(arguments, False)
        result = infa.runit(infa.arguments)
        if result.rc != 0:
            raise AirflowException("RunScorecard failed.")
