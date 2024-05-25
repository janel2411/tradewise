from pymongo import MongoClient
import certifi

client = MongoClient(
    'mongodb+srv://e1156808:OZ9wM6NhvmzElqCO@tradewisecluster.itzxyju.mongodb.net/',
    tlsCAFile=certifi.where()
)
db = client['tradewise_db']