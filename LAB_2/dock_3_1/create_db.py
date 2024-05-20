from pymongo import MongoClient # код ,в плане логики реализации , тот же самый, за исключением того, что у нас уже есть приложение , работающее в сети mynetwork , которое взаимодействует с контейнером монго , запущенном в той же сети.

client = MongoClient('mongodb://mongodb_container:27017/')  # на основе класса mongoclient создаем объект, представляющий из себя подключение к серверу монго по имени хоста mongodb_container, " работающему " на порту 27017 
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

