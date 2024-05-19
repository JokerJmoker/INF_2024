import os
from pymongo import MongoClient

# Используем переменные окружения для конфигурации подключения к MongoDB
mongo_host = os.getenv('MONGO_DB_ADDR', 'mongo')
mongo_port = int(os.getenv('MONGO_DB_PORT', 27017))
db_name = os.getenv('DB', 'testdb')

# Создаем клиент для подключения к MongoDB
client = MongoClient(mongo_host, mongo_port)
db = client[db_name]
collection = db['collection']

# Создаем документы и вставляем их в коллекцию
documents = [{"tags": f"obj_{i}"} for i in range(6)]
result = collection.insert_many(documents)

# Выводим документы для проверки
documents = collection.find({})
print("Documents found:")
for doc in documents:
    print(doc)
