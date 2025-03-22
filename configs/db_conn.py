import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_BD")

_client = MongoClient(MONGO_URI)  # create client just one time
print(f"MONGO_DB_NAME: {repr(MONGO_DB_NAME)}")
db = _client[MONGO_DB_NAME]  # db already set up

def get_database():
    """Return a instance of db, without creating a new connection"""
    return db

