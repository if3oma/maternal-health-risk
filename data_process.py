from pymongo import MongoClient
import pandas as pd
from class_load import DataBaseManager

class DataProcess:
    def __init__(self, oop_dbms):
        self.oop_dbms = oop_dbms
        self.data = oop_dbms.fetch_my_data(collection_name='maternal_care')
        self.train_data = None
        self.eval = None

    def split_data(self, train_size=0.8):
        self.train_data = self.data.sample(frac=train_size, random_state=0)
        self.eval = self.data.drop(self.train_data.index)

        return self.train_data, self.eval
        


oop_dbms = DataBaseManager(database_name='Ifeoma_Care', collection_name='Maternal_Health_Care')
data_proc = DataProcess(oop_dbms=oop_dbms)
data_proc.split_data()


