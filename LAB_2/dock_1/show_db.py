from pymongo import MongoClient

def get_object_id(collection_name, object_tag):
   
    client = MongoClient('mongodb://localhost:27017/')
  
    db = client['mydb']
    
    collection = db[collection_name]
    
    object_data = collection.find_one({"tags": object_tag})
    if object_data:
        print(f"Идентификатор объекта {object_tag} в коллекции {collection_name}: {object_data['_id']}")
    else:
        print(f"Объект {object_tag} не найден в коллекции {collection_name}")


get_object_id("mycollection", "obj_1")
