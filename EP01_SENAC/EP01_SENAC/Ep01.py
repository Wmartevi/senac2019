from pymongo import MongoClient
from datetime import datetime
import json, requests, uuid

client = MongoClient()

client = MongoClient('localhost', 27017)

db = client.ep01_database

response = requests.get("http://localhost:3000/api/v1/products.json?token=e0c91507ca69781a03c62aabd83246ed75e8ed0f498a4652")
now = datetime.now()
timestamp = now.strftime("%d-%b-%Y (%H:%M:%S.%f)")

itens = json.loads(response.text)

for item in itens["products"]:
    uid = uuid.uuid1()
    produto = {
        'unique_id': uid.hex,
        'data': now,
        'timestamp': timestamp,
        'id': item['id'],
        'name': item['name'],
        'price': item['price']
    }
    db.ep01_collection.insert_one(produto)
