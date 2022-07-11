import requests
from bs4 import BeautifulSoup as bs
import wget 

URL = "https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
data_path = "/Users/berkkayi/Desktop/aws_data_engineering_masterclass/dataset/raw_data"

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
                wget.download(link,out=data_path + "/" + filename)
                print("downloading data",filename)
            except: 
                #some data is not avaliable for past data, I passed these datas.
                print("downloading passed ",filename)
                continue  
            