from airflow.models import BaseOperator
from airflow import utils as airflow_utils, AirflowException

from execution import runMapping
from InformaticaPlugin.operators import available_arguments


class ExecuteMapping(BaseOperator):

    @airflow_utils.apply_defaults
    def __init__(self, **kwargs):
        self.infa_arguments = []
        for key, value in kwargs.items():
            if key in available_arguments:
                self.infa_arguments.append(available_arguments[key] + " " + '"' + value + '"')
            else:
                print(
                    "unrecognized key >" + key + "< provided. Its provided value is >" + value + "<. Argument IGNORED.")

        super(ExecuteMapping, self).__init__(
            **kwargs)

    def execute(self, context):
        print("dag: " + self.dag.full_filepath)
        print("dag_id: " + self.dag_id)
        print("task_type: " + self.task_type)
        print("task id: " + self.task_id)
        print("infa_arguments count: " + str(self.infa_arguments.count()))
        print("infa_arguments: " + self.infa_arguments)

        infa = runMapping.ExecuteInformaticaMapping(self.infa_arguments, False)
        result = infa.runit(infa.arguments)
        if result.rc != 0:
            raise AirflowException("RunMapping failed: " + result.message)
