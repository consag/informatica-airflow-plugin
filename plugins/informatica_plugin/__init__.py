from __future__ import division, absolute_import, print_function

from airflow.plugins_manager import AirflowPlugin

from informatica_plugin import blueprints
from informatica_plugin.operators.run_mapping import RunMapping


# Defining the plugin class
from informatica_plugin.operators.run_profile import RunScorecard
from informatica_plugin.operators.run_scorecard import RunProfile


class InformaticaPlugin(AirflowPlugin):
    name = "informatica_plugin"
    operators = [
        RunMapping,
        RunProfile,
        RunScorecard
    ]
    hooks = []
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = [blueprints.TriggerBlueprint]
    menu_links = []

