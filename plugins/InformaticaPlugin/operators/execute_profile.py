from airflow.models import BaseOperator
from airflow import utils as airflow_utils, AirflowException

from execution import runProfile

class ExecuteProfile(BaseOperator):

    @airflow_utils.apply_defaults
    def __init__(self, profile_path, **kwargs):
        self.profile_path = profile_path
        super(ExecuteProfile, self).__init__(
            **kwargs)

    def execute(self, context):
        print("dag: " + self.dag.full_filepath)
        print("dag_id: " + self.dag_id)
        print("task_type: " + self.task_type)
        print("task id: " + self.task_id)
        print("profile_path: " + self.profile_path)
        arguments = [
            "-p",
            self.profile_path,
            # TODO: the others to be added
        ]
        infa = runProfile.ExecuteInformaticaProfile(arguments, False)
        result = infa.runit(infa.arguments)
        if result.rc != 0:
            raise AirflowException("RunProfile failed.")
