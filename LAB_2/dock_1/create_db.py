from pymongo import MongoClient # испортируем класс из pymongo, с помощью которого мы будем взаимодействовать с бд

# создаем объект , указываем адрес и порт для подключения к серверу монго 
client = MongoClient('mongodb://localhost:27017/')
# в общем случае получаем коллекию и бвзу данных по соотвествующим именам. Здесь же мы их создаем 
db = client['testdb']
collection = db['collection']

# вставка документов в коллекцию(пока просто циклом, затем я буду использовать генератор)
for i in range(6):
    document = {"tags": f"obj_{i}"} # создаем словарь с ключем tags / Причем f используется для создания строки с форматом, поддерживающим запись вместо i конуертных значений 
    result = collection.insert_one(document) # вставка в коллекцию 
    print(f"New document {i} id:", result.inserted_id)

# вывод бд
documents = collection.find({})
print("Documents found:")
for doc in documents:
    print(doc)