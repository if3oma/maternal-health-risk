from pymongo import MongoClient
import pandas as pd

health = pd.read_csv('Maternal Health Risk Data Set.csv')

# print(health.head())


client = MongoClient('localhost', 27017)

# print(client.server_info())

# Create my database
db = client['maternal_health_info']
# Create my database collection
collection = client['test_collection']

# Insert our data into collection
my_data = health.to_dict(orient='records')

my_result = db.maternal_health.insert_many(my_data)

print(db.maternal_health.find_one())