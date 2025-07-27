import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
MONGO_DB_NAME = os.getenv("MONGODB_DB")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB_NAME]
chat_logs = db["chat_logs"]
