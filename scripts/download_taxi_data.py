import requests
from bs4 import BeautifulSoup as bs
import wget 
import os
from dotenv import load_dotenv
load_dotenv()

URL = "https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page"


# html parsing for target URL
r= requests.get(URL)
soup = bs(r.text,"html.parser")

data_link = []
data_metadata = []
# filtering list content from html with beatifulsoup
for li in soup.find_all("li"):
    for a in li.find_all("a"):
        if ".parquet" in str(a.get("href")) :
            # cathing link and filename from parsed html
            link = str(a.get("href"))
            filename = link.split("/")[-1]
            try:
                #downloading data from link to output path.
                wget.download(link,out=os.getenv("RAW_DATA_PATH") + "/" + filename)
                print("downloading data",filename)
            except: 
                #some data is not avaliable for past data, I passed these datas.
                print("downloading passed ",filename)
                continue  
            