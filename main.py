from class_load import DataBaseManager
from data_process import DataProcess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

#define the class "ModelBuild" for building, training and evaluating the machine learning
class ModelBuild:
    def __init__(self, oop_dbms, data_proc):
        self.data_proc = data_proc
        self.oop_dbms = oop_dbms
        self.model = DecisionTreeClassifier()  #create a model of Decision Tree Classifier
        self.prediction = None
        self.train_data = data_proc.train_data #access the training data from the data processer
        self.eval = data_proc.eval   #access the training data from the data processor

     
    def train_model(self):
        d = {'low risk':0, 'mid risk':1, 'high risk':2}
        self.train_data['RiskLevel'] = self.train_data['RiskLevel'].map(d)
        X = self.train_data.drop(columns='RiskLevel')
        y = self.train_data['RiskLevel']

        self.model.fit(X, y)
        print('Model Trained!!!!')

    def predict(self):
        d = {'low risk':0, 'mid risk':1, 'high risk':2}
        self.eval['RiskLevel'] = self.eval['RiskLevel'].map(d)
        test = self.eval.drop(columns='RiskLevel')
        self.prediction = self.model.predict(test)

    def evaluate(self):
        evaluation = accuracy_score(self.eval['RiskLevel'], self.prediction)
        print(evaluation)

    def save_model(self):
        pickle.dump(self.model, open('model.pkl', 'wb'))