from airflow.plugins_manager import AirflowPlugin
from InformaticaPlugin import blueprints
from InformaticaPlugin.operators.execute_mapping import ExecuteMapping


# Defining the plugin class
from InformaticaPlugin.operators.execute_profile import ExecuteProfile
from InformaticaPlugin.operators.execute_scorecard import ExecuteScorecard


class InformaticaPlugin(AirflowPlugin):
    name = "InformaticaPlugin"
    operators = [
        ExecuteMapping,
        ExecuteProfile,
        ExecuteScorecard
    ]
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [blueprints.TriggerBlueprint]
    menu_links = []

