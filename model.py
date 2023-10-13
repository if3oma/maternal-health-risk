from class_load import DataBaseManager
from data_process import DataProcess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


class ModelBuild:
    def __init__(self, oop_dbms, data_proc):
        self.data_proc = data_proc
        self.oop_dbms = oop_dbms
        self.data = oop_dbms.fetch_my_data(collection_name='maternal_care')
        self.model = DecisionTreeClassifier()
        self.prediction = None
        self.train_data = None
        self.eval = None

    def train_model(self):
        self.train_data, self.eval = self.data_proc.split_data()
        d = {'low risk':0, 'mid risk':1, 'high risk':2}
        self.train_data['RiskLevel'] = self.train_data['RiskLevel'].map(d)
        X = self.train_data.drop(columns='RiskLevel')
        y = self.train_data['RiskLevel']

        self.model.fit(X, y)
        print('Model Trained!!!!')

    def predict(self):
        self.train_data, self.eval = self.data_proc.split_data()
        d = {'low risk':0, 'mid risk':1, 'high risk':2}
        self.eval['RiskLevel'] = self.eval['RiskLevel'].map(d)
        test = self.eval.drop(columns='RiskLevel')
        self.prediction = self.model.predict(test)

        print(self.prediction.shape)

    def evaluate(self):
        evaluation = accuracy_score(self.eval['RiskLevel'], self.prediction)
        print(evaluation)

oop_dbms = DataBaseManager(database_name='Ifeoma_Care', collection_name='Maternal_Health_Care')
data_proc = DataProcess(oop_dbms=oop_dbms)

models = ModelBuild(oop_dbms=oop_dbms, data_proc=data_proc)
models.train_model()
models.predict()
models.evaluate()