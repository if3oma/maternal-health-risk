from class_load import DataBaseManager
from data_process import DataProcess
from model import ModelBuild

oop_dbms = DataBaseManager(database_name='Ifeoma_Care')
data_proc = DataProcess()

data_proc.load_my_data()
oop_dbms.insert_data(collection_name='maternal_care', data=data_proc.data)
oop_dbms.fetch_my_data(collection_name='maternal_care')
data_proc.split_data()

models = ModelBuild(oop_dbms=oop_dbms, data_proc=data_proc)

models.train_model()
models.predict()
models.evaluate()
models.save_model()