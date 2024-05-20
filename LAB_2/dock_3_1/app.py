from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://mongodb_container:27017/')
db = client['testdb']
collection = db['collection']

@app.route('/')
def index():
    documents = collection.find({})
    texts = [doc['tags'] for doc in documents]
    return render_template('index.html', data=texts)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')