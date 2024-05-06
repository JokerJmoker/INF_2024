from flask import Flask, render_template
# добавили возможность динамически встраивать данные в сайт
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongo", 27017)  

@app.route('/')
def index():
    # пишем начальные данные 
    db = client.testdb  
    collection = db.collection 
    # ищем все в бд
    
    documents = collection.find({})
    return render_template('index.html', data=documents)
    

    
if __name__ == '__main__':
    # запукскаем в режиме отладки , и ставим хост нулевой, чтобы можно было зайти извне
    app.run(debug=True, host='0.0.0.0')
    