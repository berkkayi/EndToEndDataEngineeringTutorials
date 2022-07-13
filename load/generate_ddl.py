import os
from dotenv import load_dotenv
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
from sqlalchemy import create_engine
load_dotenv()

conne = create_engine('redshift+psycopg2://{}:{}@{}:{}/{}'.format(os.getenv("REDSHIFT_ADMIN_USERNAME"),
                                                            os.getenv("REDSHIFT_ADMIN_PASSWORD"),
                                                            os.getenv("REDSHIFT_HOST"),
                                                            os.getenv("REDSHIFT_PORT"),
                                                            os.getenv("REDSHIFT_DB")))
table_names = ["yellow_taxi_trip","green_taxi_trip","fhv_trip","fhvhv_trip"]
file_names = ["yellow_tripdata_2022-04.parquet","green_tripdata_2022-04.parquet","fhv_tripdata_2022-04.parquet","fhvhv_tripdata_2022-04.parquet"]
ddl_location = os.getenv("PROJECT_ROOT_PATH") + "load/sql_ddl/"

def get_ddl(table_name,file_name,schema_name,connection):
    file = pq.read_table(os.getenv("PROJECT_ROOT_PATH") +\
        f"/dataset/raw_data/{file_name}")
    batch = file.to_batches(100)[0]
    sample_df = batch.to_pandas()
    table_name = schema_name + "." + table_name
    return pd.io.sql.get_schema(sample_df,name=table_name,con=connection)

def save_sql_result(sql_str,table_name,target_location):
    with open(target_location + table_name + ".sql","w") as f:
        f.write(sql_str)

for table_name,file_name in zip(table_names,file_names):
    
    ddl = get_ddl(table_name,file_name,"taxi_trip",conne)
    save_sql_result(ddl,table_name,ddl_location)
    print(table_name," ddl sql saved to load/sql_ddl/ path.")