You should install with pip awscli for installing aws command line interface.
- pip install awscli

create virtualenv for x86_64 architecture (it required for macos m1)
- /usr/local/Homebrew/bin/python3.9 -m venv de_env
- source de_env/bin/activate
- pip install --upgrade pip && pip install -r requirements.txt

Data source is a taxi trip data from New York. I downloaded from below link:
- https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Dataset between 2009 to current date. Totally data size is 42 GB. If you want to know more details of dataset, you can check the link.

If you don't connect redshift cluster from local, you must create a new VPC that allow your ip address or public routing.

For your using PGadmin, you should sign in your browser as localhost:8081. After that you can access postgre db and see monitoring db.

Airflow installation:

- mkdir airflow 
- cd airflow 
- mkdir -p ./dags ./logs ./plugins 
- echo -e "AIRFLOW_UID=$(id -u)" > .env 
- curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml' 
- docker-compose airflow-init
- docker-compose up 

airflow webserver--> localhost:8080  (user=airflow,pwd=airflow)