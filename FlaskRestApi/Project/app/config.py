from pymongo import MongoClient


class Config:
    MONGO_URI = "mongodb://localhost:27017/Promantus"
    client = MongoClient(MONGO_URI)
    db = client['Promantus']
    collection = db['FlaskRestApi']



