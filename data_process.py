from pymongo import MongoClient
import pandas as pd
from class_load import DataBaseManager

class DataProcess:
    def __init__(self):
        self.data = None
        self.train_data = None
        self.eval = None

    def load_my_data(self):
        self.data = pd.read_csv('Maternal Health Risk Data Set.csv')
        return self.data

    def split_data(self, train_size=0.8):
        self.train_data = self.data.sample(frac=train_size, random_state=0)
        self.eval = self.data.drop(self.train_data.index)

