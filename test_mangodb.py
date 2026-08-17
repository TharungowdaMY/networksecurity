import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# 1. Correct URI without < > around password
uri = "mongodb+srv://tharungowda0104_db_user:TZshuig123@cluster0.vqalrcu.mongodb.net/?appName=Cluster0"

# 2. Add tlsCAFile using certifi
client = MongoClient(
    uri,
    server_api=ServerApi('1'),
    tlsCAFile=certifi.where()
)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error:", e)