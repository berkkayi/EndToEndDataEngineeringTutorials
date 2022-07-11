import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3_clinet = boto3.client("s3",
                        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                        aws_secret_access_key=os.getenv("AWS_SECREC_ACCESS_KEY"))
s3_clinet.list_buckets()














