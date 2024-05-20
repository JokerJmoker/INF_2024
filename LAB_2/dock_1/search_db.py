from pymongo import MongoClient
from bson.objectid import ObjectId # преобразвем строковый идентификатор монго в объект objectId для дальнейшей работы 

def print_object_info_by_id( object_id): # эта функция - просто пример работы с бд и не претендует на универсальность в своем использовании 
   
    client = MongoClient('mongodb://localhost:27017/')
    
    db = client['testdb']
    
    collection = db['collection']
   
    object_data = collection.find_one({"_id": ObjectId(object_id)}) # исползуем метод библиотки 
    if object_data:
        print("Информация об объекте с id", object_id)
        for key, value in object_data.items():
            print(f"{key}: {value}")
    else:
        print(f"Объект с id {object_id} не найден в этой коллекции ")


print_object_info_by_id("664a7a8921d81c3f772a666e")

