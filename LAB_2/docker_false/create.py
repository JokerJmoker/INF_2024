from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')

db = client['testdb']

collection = db['collection']

document = {"tags": "obj_777"}
result = collection.insert_one(document)
print("new document id:", result.inserted_id)

documents = collection.find({})
print("Documents found:")
for doc in documents:
    print(doc)


