import requests
from bs4 import BeautifulSoup as bs
import wget 
import re
URL = "https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
data_path = "/Users/berkkayi/Desktop/aws_data_engineering_masterclass/dataset"
r= requests.get(URL)
soup = bs(r.text,"html.parser")

data_link = []
data_metadata = []
for li in soup.find_all("li"):
    for a in li.find_all("a"):
        if ".parquet" in str(a.get("href")) :
            link = str(a.get("href"))
            filename = link.split("/")[-1]
            try:
                wget.download(link,out=data_path + "/" + filename)
                print("downloading data",filename)
            except: 
                print("downloading passed ",filename)
                continue  
            