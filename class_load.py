from pymongo import MongoClient
import pandas as pd

health = pd.read_csv('Maternal Health Risk Data Set.csv')
my_data = health.to_dict(orient='records')

class DataBaseManager:
    def __init__(self, database_name, collection_name):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[database_name]
        self.collection = self.client[collection_name]
        self.data = None

    # Insert
    def insert_data(self, data):
        self.db.maternal_care.insert_many(data)

    #Fetch data
    def fetch_my_data(self, collection_name):
        collection = self.db[collection_name]
        self.data = pd.DataFrame(list(collection.find()))
        self.data = self.data.drop(columns='_id')
        return self.data
    
    # Split data



# oop_dbms.insert_data(data=my_data)

# all_data = oop_dbms.fetch_my_data(collection_name='maternal_care')
# print(all_data.head())


