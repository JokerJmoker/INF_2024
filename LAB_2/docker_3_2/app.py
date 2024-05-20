import os
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Используем переменные окружения для конфигурации подключения к MongoDB
mongo_host = os.getenv('MONGO_DB_ADDR', 'mongo')
mongo_port = int(os.getenv('MONGO_DB_PORT', 27017))
db_name = os.getenv('DB', 'testdb')

# Создаем клиент для подключения к MongoDB
client = MongoClient(mongo_host, mongo_port)
db = client[db_name]
collection = db['collection']

@app.route('/')
def index():
    documents = collection.find({})
    texts = [doc['tags'] for doc in documents]
    return render_template('index.html', data=texts)


# здесь мы убрали строку на проверку того, запущен ли этот скрипт напрямую, а не импортируется в виде модлуя ( составляющей ) другими скриптами.С точки зрения рефакторинга ее следует сотавить, однако для нашей задачи можно и опустить  

app.run(debug=True, host='0.0.0.0')
