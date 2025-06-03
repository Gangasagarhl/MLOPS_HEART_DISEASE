import pymongo
import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()


MONGO_DB_URL="mongodb+srv://sagar:gatE2024%401@cluster0.ikkbwln.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
print(MONGO_DB_URL, "\n\n")

class Load:
    
    def __init__(self):
        print("Loading to the database")

    def insert_data_mongodb(self,records,database,collection):
        print("Now trying to insert into the Mongodb atlas\n")
        print("INFO: ", database, collection )
        self.database=database
        self.collection=collection
        self.records=records

        self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
        print(MONGO_DB_URL)
        self.database = self.mongo_client[self.database]
            
        self.collection=self.database[self.collection]
        self.collection.insert_many(self.records)
        print("Length: ",len(self.records))

        return(len(self.records))
        
        
        
