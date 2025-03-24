import os
import logging
from dotenv import load_dotenv
from pymongo import MongoClient

logger = logging.getLogger(__name__)

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")


def get_database():
    """Establishes and returns a connection to the MongoDB"""
    
    try:
        client = MongoClient(MONGO_URL)
        db = client[MONGO_DB]
        db.command("ping")
        logger.info("Connection sucessful with mongoDB")
        return db
    except ConnectionError as e:
        logger.error(f"Connection Failure wihth mongoDB: {e}")
        raise RuntimeError("Error to connect to database")
    except Exception as e:
        logger.error(f"Unexpected error to connect to database: {e}")
        raise RuntimeError("Unknow Error to connect to database")
    