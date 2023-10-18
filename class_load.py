from pymongo import MongoClient
import pandas as pd


class DataBaseManager:
    def __init__(self, database_name):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[database_name]
        self.data = None

    # Insert
    def insert_data(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_many(data.to_dict(orient='records'))

    #Fetch data
    def fetch_my_data(self, collection_name):
        collection = self.db[collection_name]
        self.data = pd.DataFrame(list(collection.find()))
        self.data = self.data.drop(columns='_id')
    