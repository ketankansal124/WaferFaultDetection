from pymongo.mongo_client import MongoClient
import pandas as pd
import json
from dotenv import load_dotenv
import os

load_dotenv()

#URL
URL=os.getenv("MONGO_DB_URL")
#Create a new client and connect to server
client = MongoClient(URL)

#Create database name and collection name
DATABASE_NAME=os.getenv("MONGO_DATABASE_NAME")
COLLECTION_NAME=os.getenv("MONGO_COLLECTION_NAME")

df=pd.read_csv("notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)