#Import pymongo library for working with MongoDB
from pymongo import MongoClient
#import pandas library to provide structure
import pandas as pd

#create a class to manage interactions with MongoDB
class DataBaseManager:
    #initialize the class with a constructor
    def __init__(self, database_name):
        #connect to the MongoDB on the host computer
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[database_name]
        self.data = None

    #insert data into collection
    def insert_data(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_many(data.to_dict(orient='records'))

    #Fetch data from the collection in the database
    def fetch_my_data(self, collection_name):
        collection = self.db[collection_name]
        #store all the data in the pandas DataFrame
        self.data = pd.DataFrame(list(collection.find()))
        #get rid of the "id" column because it is not relevant to the model
        self.data = self.data.drop(columns='_id')
    