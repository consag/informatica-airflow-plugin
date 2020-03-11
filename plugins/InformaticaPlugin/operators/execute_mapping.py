from airflow.models import BaseOperator
from airflow import utils as airflow_utils, AirflowException

from execution import runMapping
from InformaticaPlugin.operators import available_arguments
import os


class ExecuteMapping(BaseOperator):

    @airflow_utils.apply_defaults
    def __init__(self, **kwargs):
        self.infa_arguments = []
        self.pre_command = None
        for key, value in kwargs.items():
            if key == 'target':
                self.pre_command = '. ' + os.environ.get('configDir', '.') + '/scheduler_env.' + value + '.sh'
            else:
                if key in available_arguments:
                    self.infa_arguments.append(available_arguments[key] + " " + value)

        super(ExecuteMapping, self).__init__(
            **kwargs)

    def execute(self, context):
        print("dag: " + self.dag.full_filepath)
        print("dag_id: " + self.dag_id)
        print("task_type: " + self.task_type)
        print("task id: " + self.task_id)
        print("infa_arguments: " + ' '.join(self.infa_arguments))
        if self.pre_command is None:
            print("no pre_command provided.")
        else:
            print("pre_command: " + self.pre_command)

        infa = runMapping.ExecuteInformaticaMapping(self.infa_arguments, log_on_console=False,
                                                    pre_command=self.pre_command)
        result = infa.runit(infa.arguments)
        if result.rc != 0:
            raise AirflowException("RunMapping failed: " + result.message)
