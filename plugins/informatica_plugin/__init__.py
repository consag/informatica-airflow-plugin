from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin

from informatica_plugin import blueprints
from informatica_plugin.operators.execute_mapping import ExecuteMapping


# Defining the plugin class
from informatica_plugin.operators.execute_profile import ExecuteProfile
from informatica_plugin.operators.execute_scorecard import ExecuteScorecard


class InformaticaPlugin(AirflowPlugin):
    name = "informatica_plugin"
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

