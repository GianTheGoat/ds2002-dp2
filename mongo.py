from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
import json

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
client = MongoClient(uri, username='nmagee', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)
# specify a database
db = client.gianDB
# specify a collection
collection = db.gianCN

# assuming you have defined a connection to your db and collection already:

# Loading or Opening the json file
# with open('data.json') as file:

directory = "data"
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as f:
        try:
            file_data = json.load(f)
            print(f, "successful")
            try:
                collection.insert_many(file_data)
            except Exception as e:
                print("Mongo import error")
        except Exception as e:
            print(e)
            print(f, "failure")


# Inserting the loaded data in the collection
# if JSON contains data more than one entry
# insert_many is used else insert_one is used

# if isinstance(file_data, list):
#     collection.insert_many(file_data)  
# else:
#     collection.insert_one(file_data)