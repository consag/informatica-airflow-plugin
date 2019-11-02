from setuptools import setup

setup(
    name='informatica-airflow-plugin',
    version='0.1',
    packages=['plugins', 'plugins.informatica_plugin', 'plugins.informatica_plugin.operators',
              'plugins.informatica_plugin.blueprints', 'informatica_plugin', 'informatica_plugin.operators',
              'informatica_plugin.blueprints'],
    package_dir={'': 'plugins'},
    url='https://github.com/jacbeekers/informatica-airflow-plugin',
    license='MIT',
    author='Jac. Beekers',
    author_email='beekersjac@gmail.com',
    description='Airflow Plugin for Informatica Platform'
)
