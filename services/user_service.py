from configs.log_config import logger
from models.user_model import User
from storages.user_storage import UserStorage

class UserService:
    
    @staticmethod
    def create_user(user_data: dict) -> User:
        """Transform google user data in object user and save ind db"""
        try:
            user = User(
                google_id=user_data["id"],
                email=user_data["email"],
                verified_email=user_data["verified_email"],
                name=user_data["name"],
                given_name=user_data["given_name"],
                family_name=user_data["family_name"],
                picture=user_data["picture"]
            )
            saved_user = UserStorage.save_user(user)
            logger.info(f"User saved: {saved_user.google_id}")
            return saved_user
        except KeyError as e:
            logger.warning(f"User missing data: {e}")
            raise ValueError(f"required data missing: {e}")
    
        except Exception as e:
            logger.error(f"Error while creating user: {e}")
            raise RuntimeError("Error while processing user")