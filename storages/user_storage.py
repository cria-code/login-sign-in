"""
Module for managing User data.
"""
from pymongo.errors import PyMongoError
from models.user_model import User
import logging
from configs.db_conn import get_database


class UserStorage:
    """
    This class handles User data in the MongoDB database.
    """
    def __init__(self, db_connection=get_database()):
        self.db = db_connection
        self.collection = db_connection.get_collection("users")
        self.logger = logging.getLogger(__name__)

    def save_user(self, user_data: dict) -> User:
        """Saves or updates a user in the database."""
        self.logger.info("Saving or Updating a User in DataBase")
        try:
            self.collection.update_one(
                {"id": user_data["id"]},
                {"$set": user_data},
                upsert=True
            )
            self.logger.info(
                "User %s saved or updated successfully.", user_data["id"])

        except PyMongoError as ex:
            self.logger.error("Failed to save user: %s", ex)
            raise
        except ValueError as ex:
            self.logger.error("Validation error: %s", ex)
            raise
