import os
import requests
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from urllib.parse import urlencode
from dotenv import load_dotenv
from fastapi import HTTPException
from services.user_service import UserService

load_dotenv()

router = APIRouter()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URL = os.getenv("GOOGLE_REDIRECT_URL")
GOOGLE_AUTH_URL = os.getenv("GOOGLE_AUTH_URL")
GOOGLE_TOKEN_URL = os.getenv("GOOGLE_TOKEN_URL")
GOOGLE_SCOPES = os.getenv("GOOGLE_SCOPES").split(",")

class GoogleAuthService:
    @staticmethod
    @router.get("/auth/login")
    def login():
        """Redirect for login page"""
        params = {
            "client_id": GOOGLE_CLIENT_ID,
            "response_type": "code",
            "scope": " ".join(GOOGLE_SCOPES),
            "redirect_uri": GOOGLE_REDIRECT_URL,
            "access_type": "offline",
            "prompt": "consent"
        }
        print(f"Redirect URI: {GOOGLE_REDIRECT_URL}")
        return RedirectResponse(f"{GOOGLE_AUTH_URL}?{urlencode(params)}")

    @staticmethod
    @router.get("/auth/callback")
    def callback(code:str):
        """Receive an autorization code and change for a access token"""
        data = {
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": GOOGLE_REDIRECT_URL
        }
        response = requests.post(GOOGLE_TOKEN_URL, data=data)
        token_json = response.json()
        
        if "access_token" not in token_json:
            raise HTTPException(status_code=400, detail="Autentication failed")
        
        user_data = UserService.get_extra_info(token_json["access_token"])
        
        user = UserService.create_user(user_data)
        
        return {"user_info": user.model_dump(), "tokens": token_json}
        
        