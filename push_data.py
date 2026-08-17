import os
import sys
import json
from dotenv import load_dotenv 

load_dotenv()

MANGO_DB_URL = os.getenv("MANGO_DB_URL")
print(MANGO_DB_URL)

import certifi
ca=certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException  
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            #self.client = pymongo.MongoClient(MANGO_DB_URL, tlsCAFile=ca)
            #self.db = self.client['NetworkSecurity']
            #self.collection = self.db['network_data']
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) 

    def csv_to_json(self, file_path):
        try:
            #df = pd.read_csv(csv_file_path)
            #df.to_json(json_file_path, orient='records', lines=True)
            #logging.info(f"Converted {csv_file_path} to {json_file_path}")
            data=pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_data_mango(self, records,database,collection):
        try:
            #self.collection.insert_many(records)
            #logging.info(f"Inserted {len(records)} records into MongoDB")
            self.database=database
            self.collection=collection
            self.records=records
            self.mango_client = pymongo.MongoClient(MANGO_DB_URL)
            self.database=self.mango_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
if __name__=="__main__":
    FILE_PATH="Network_Data\phisingData.csv"
    DATABASE="NetworkSecurity"
    Collection="networkData"
    networkobj= NetworkDataExtract()
    records=networkobj.csv_to_json(file_path=FILE_PATH)
    print(records)
    no_of_records=networkobj.insert_data_mango(records=records,database=DATABASE,collection=Collection)
    print(no_of_records)