from airflow.plugins_manager import AirflowPlugin
from InformaticaPlugin import blueprints
from InformaticaPlugin.operators.execute_mapping import ExecuteMapping
from InformaticaPlugin.operators.execute_profile import ExecuteProfile
from InformaticaPlugin.operators.execute_scorecard import ExecuteScorecard
from InformaticaPlugin.operators.execute_workflow import ExecuteWorkflow


class InformaticaPlugin(AirflowPlugin):
    name = "InformaticaPlugin"
    operators = [
        ExecuteMapping,
        ExecuteProfile,
        ExecuteScorecard,
        ExecuteWorkflow
    ]
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [blueprints.TriggerBlueprint]
    menu_links = []

