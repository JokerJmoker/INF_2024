from pymongo import MongoClient
from bson.objectid import ObjectId

def print_object_info_by_id(collection_name, object_id):
   
    client = MongoClient('mongodb://localhost:27017/')
    
    db = client['testdb']
    
    collection = db[collection_name]
   
    object_data = collection.find_one({"_id": ObjectId(object_id)})
    if object_data:
        print("Информация о объекте с id", object_id)
        for key, value in object_data.items():
            print(f"{key}: {value}")
    else:
        print(f"Объект с id {object_id} не найден в коллекции {collection_name}")


print_object_info_by_id("collection", "6627bccdb6c930e7ea34d633")

