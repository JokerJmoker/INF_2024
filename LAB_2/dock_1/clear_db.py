from pymongo import MongoClient # очищаем бд при помощи изветсных методов

client = MongoClient('mongodb://localhost:27017/')

db = client['testdb']

client.drop_database(db)

print("База данных успешно удалена")

