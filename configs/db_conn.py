import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")


def get_database():
    """
    Establishes and returns a connection to the MongoDB database.
    """
    client = MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    print(MONGO_DB)
    return db