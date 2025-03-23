from models.user_model import User
from storages.user_storage import UserStorage

# GOOGLE_PEOPLE_URL = os.getenv("GOOGLE_PEOPLE_URL")

class UserService:
    @staticmethod
    def create_user(user_data: dict) -> User:
        """Transform google user data in object user and save ind db"""
        user = User(
            google_id=user_data["id"],
            email=user_data["email"],
            verified_email=user_data["verified_email"],
            name=user_data["name"],
            given_name=user_data["given_name"],
            family_name=user_data["family_name"],
            picture=user_data["picture"],
            # birthdate=user_data.get("birthdays", [{}])[0].get("date"),
            # gender=user_data.get("genders", [{}])[0].get("value")
        )

        return UserStorage.save_user(user)
        
    
    # def get_info(access_token: str):
    #     """get birthdate and gender"""
        
    #     headers = {"Authorization": f"Bearer {access_token}"}
        
    #     response = requests.get(GOOGLE_USERINFO_URL, headers=headers)
    #     user_info = response.json()
        
    #     # people_params = {"personFields": "birthdays, genders"}
    #     # response_people = requests.get(GOOGLE_PEOPLE_URL, headers=headers, params=people_params)
    #     # people_info = response_people.json()
        
    #     # user_info["birthdays"] = people_info.get("birthdays", [])
    #     # user_info["genders"] = people_info.get["genders", []]
        
    #     return user_info