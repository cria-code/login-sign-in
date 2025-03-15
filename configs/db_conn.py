import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_BD")


def get_database():
    client = MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    return db
