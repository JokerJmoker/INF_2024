from pymongo import MongoClient

client = MongoClient('mongodb://mongodb_container:27017/') # НА ЭТОЙ СТРОЧКЕ ОШИБКА ПРИ ЗАПУСКЕ КОНТЕЙНЕРА 
db = client['testdb']
collection = db['collection']

# вставка документов в коллекцию
for i in range(6):
    document = {"tags": f"obj_{i}"}
    result = collection.insert_one(document)
    print(f"New document {i} id:", result.inserted_id)

# вывод бд
documents = collection.find({})
print("Documents found:")
for doc in documents:
    print(doc)