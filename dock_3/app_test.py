from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongodb_container:27017/') # подключение к бд 
db = client['testdb']
collection = db['collection']

@app.route('/')
def index():
    documents = collection.find({})
    texts = [doc['text'] for doc in documents]  # Извлекаем текст из каждого документа
    return render_template('index.html', data=texts)

if __name__ == '__main__':
    # запукскаем в режиме отладки , и ставим хост нулевой, чтобы можно было зайти извне
    app.run(debug=True, host='0.0.0.0')
