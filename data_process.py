from pymongo import MongoClient
import pandas as pd
from class_load import DataBaseManager

#define a class for data processing operations
class DataProcess:
    def __init__(self):
        self.data = None
        self.train_data = None
        self.eval = None

#define a method to load data from CSV file
    def load_my_data(self):
       #use pandas to load the csv file
        self.data = pd.read_csv('Maternal Health Risk Data Set.csv')
        #return the loaded data
        return self.data

#define a method to spilt the loaded data into train data. 
# I used 80% of the data to give room to test the accuracy of the trained data
    def split_data(self, train_size=0.8):
        #randomly sample a fraction of the data for the training set.
        self.train_data = self.data.sample(frac=train_size, random_state=0)
        
       #create the evaluation set
        self.eval = self.data.drop(self.train_data.index)
