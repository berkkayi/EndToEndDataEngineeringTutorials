from time import sleep
from json import dumps
from kafka import KafkaProducer
import requests
from dotenv import load_dotenv
import os
load_dotenv()
url = "https://api.co2signal.com/v1/latest?countryCode=FR"

payload={}
headers = {
  'auth-token': os.getenv("STREAM_API_TOKEN")
}


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

while True:
    response = requests.request("GET", url, headers=headers, data=payload)
    producer.send("demo_1",value=response.text)
    print("producing")
    sleep(1)