docker cp dags airflow:/usr/local/airflow/
docker cp plugins airflow:/usr/local/airflow/
##
# Copy the deploy modules
docker cp ../devops-informatica-tools airflow:/usr/local/airflow

