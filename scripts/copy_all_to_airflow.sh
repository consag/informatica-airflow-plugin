docker cp dags airflow:/usr/local/airflow/
docker cp plugins airflow:/usr/local/airflow/
##
# Copy the deploy modules
docker cp ../devops-informatica-tools/execution airflow:/usr/local/airflow/plugins
docker cp ../devops-informatica-tools/supporting airflow:/usr/local/airflow/plugins
docker cp ../devops-informatica-tools/cicd airflow:/usr/local/airflow/plugins

# or just this one?
docker cp ../devops-informatica-tools airflow:/usr/local/airflow
docker cp requirements.txt airflow:/usr/local/airflow

