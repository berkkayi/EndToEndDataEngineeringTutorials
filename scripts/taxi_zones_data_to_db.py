import pandas as pd
from sqlalchemy import create_engine
import os
import wget

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')

wget.download("https://data.cityofnewyork.us/api/views/755u-8jsi/rows.csv?accessType=DOWNLOAD",
    out=os.getcwd() + "/" + "taxi_zone_lookup.csv")


df_zones = pd.read_csv('taxi_zone_lookup.csv')
df_zones.to_sql(name='zones', con=engine, if_exists='replace')