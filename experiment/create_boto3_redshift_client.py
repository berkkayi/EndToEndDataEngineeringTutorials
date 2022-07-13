import boto3
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

conn = psycopg2.connect(host=os.getenv("REDSHIFT_HOST"),
                        database=os.getenv("REDSHIFT_DB"),
                        port=os.getenv("REDSHIFT_PORT"),
                        user=os.getenv("REDSHIFT_ADMIN_USERNAME"),
                        password=os.getenv("REDSHIFT_ADMIN_PASSWORD"))

cursor = conn.cursor()
cursor.execute("SELECT DISTINCT table_name FROM information_schema.columns WHERE table_schema = 'public'")
print(cursor.fetchall())

cursor.close()
conn.close()