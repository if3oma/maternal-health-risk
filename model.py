#import necessary libraries to build the model
from class_load import DataBaseManager
from data_process import DataProcess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

#define a class 'ModelBuild' for training, predicting and evaluating the machine learning model
class ModelBuild:
    def __init__(self, oop_dbms, data_proc):
        self.data_proc = data_proc
        self.oop_dbms = oop_dbms
        self.model = DecisionTreeClassifier() #create a decision tree classifer
        self.prediction = None
        self.train_data = data_proc.train_data
        self.eval = data_proc.eval
   
   #define a method to train the machine learning model
    def train_model(self):
        #map the risk level to numerical values for training the model
        d = {'low risk':0, 'mid risk':1, 'high risk':2}
        self.train_data['RiskLevel'] = self.train_data['RiskLevel'].map(d)
        X = self.train_data.drop(columns='RiskLevel')
        y = self.train_data['RiskLevel'] #target vector is the 'Risklevel' column
        #training the model
        self.model.fit(X, y) #X is the features, y is the target vector
        print('Model Trained!!!!')
    
    #define a method to make predictions using the trained model
    def predict(self):
        d = {'low risk':0, 'mid risk':1, 'high risk':2}
        self.eval['RiskLevel'] = self.eval['RiskLevel'].map(d)
        test = self.eval.drop(columns='RiskLevel')
        self.prediction = self.model.predict(test)

    #define a method to evaluate the model's performance. I used accuracy score
    def evaluate(self):
        evaluation = accuracy_score(self.eval['RiskLevel'], self.prediction)
        print(evaluation) #print the evaluation result

    #define a method to save the trained model using pickle
    def save_model(self):
        pickle.dump(self.model, open('model.pkl', 'wb'))