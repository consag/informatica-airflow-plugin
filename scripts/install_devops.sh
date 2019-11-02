docker exec airflow pip install --user -i https://test.pypi.org/simple/ informatica-airflow-plugin==0.0.2
#docker exec airflow pip install --user -r /usr/local/airflow/requirements.txt --find-links file:///usr/local/airflow/devops-informatica-tools
docker exec airflow pip install --user /usr/local/airflow/devops-informatica-tools
#docker exec airflow pip install --user cryptography
#docker exec airflow pip install --user Crypto

