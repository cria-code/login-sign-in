from configs import db_conn
from models.user_model import User

class UserStorage:
    @staticmethod
    def save_user(user_data: User):
        """Save or update a user in BD"""
        users_collection = db_conn["users"]
        existing_user = users_collection.find_one({"google_id": user_data.google_id})
        
        if existing_user:
            users_collection.update_one({"google_id": user_data.google_id}, {"$set": user_data.model_dump()})
            print("User udated")
        else:
            users_collection.insert_one(user_data.model_dump())    
            print("User inserted")
            
        return user_data    