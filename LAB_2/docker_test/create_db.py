from pymongo import MongoClient

client = MongoClient('mongodb_container', 27017)
db = client['testdb']
collection = db['collection']

documents = [{"tags": f"obj_{i}"} for i in range(6)] # генератор
result = collection.insert_many(documents)

# Вывод бд
documents = collection.find({})
print("Documents found:")
for doc in documents:
    print(doc)