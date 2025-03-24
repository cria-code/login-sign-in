import logging
from configs import db_conn
from models.user_model import User
from pymongo.errors import PyMongoError

logger = logging.getLogger(__name__)

class UserStorage:
    
    @staticmethod
    def save_user(user_data: User):
        """Save or update a user in BD"""
        try:
            db = db_conn.get_database()
            users_collection = db["users"]
            users_collection.find_one({"google_id": user_data.google_id})
            
            users_collection.update_one(
                {"google_id": user_data.google_id},
                {"$set": user_data.model_dump()},
                upsert=True
            )
            print("User Saved or updated")
                
            for user in users_collection.find():
                print(user)    
            return user_data    
        except PyMongoError as e:
            logger.error(f"Error to access database: {e}")
            raise RuntimeError("Error to saving user on database")
        
        except Exception as e:
            logger.error(f"Unexpected error while saving useron database: {e}")
            raise RuntimeError("Unknow Error while saving user on database")