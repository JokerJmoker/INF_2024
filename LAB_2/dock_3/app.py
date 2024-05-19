import os
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

mongo_host = os.getenv('MONGO_DB_ADDR', 'localhost')
mongo_port = int(os.getenv('MONGO_DB_PORT', 27017))
db_name = os.getenv('DB', 'testdb')

client = MongoClient(mongo_host, mongo_port)
db = client[db_name]
collection = db['collection']

@app.route('/')
def index():
    documents = collection.find({})
    texts = [doc['tags'] for doc in documents]
    return render_template('index.html', data=texts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
