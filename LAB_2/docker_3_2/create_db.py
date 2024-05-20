import os # ипортируем модуль ос, чтобы  взаимодействовать с перменными окружения 
from pymongo import MongoClient # тот же класс

# используем переменные окружения для конфигурации подключения к MongoDB, извлекая из них значения(установленные в  docker-compose) при помощи os.getenv . Вообще, можно было бы их явно не указывть, поскльку передались бы значения по умолчанию(те же самые, что мы указали), однако это сильно бы снизило читабильность и понимание, потому мы их определили в compose и тут уже непосредственно к ним обратились
mongo_host = os.getenv('MONGO_DB_ADDR', 'mongo')
mongo_port = int(os.getenv('MONGO_DB_PORT', 27017))
db_name = os.getenv('DB', 'testdb')

# уже изветсная конструкция , за исключеним того, что в качетсве парметров мы принимаем пременные окружения для корректного взаимодейсвтия между контейенрами 
client = MongoClient(mongo_host, mongo_port)
db = client[db_name]
collection = db['collection']

# тут я решил использовать генератор, если говорить о рефакторингеа
documents = [{"tags": f"obj_{i}"} for i in range(6)]
result = collection.insert_many(documents)

# выводим документы для сравнения с тем, что на странице 
documents = collection.find({})
print("Documents found:")
for doc in documents:
    print(doc)
