import os
import httpx
from configs.log_config import logger
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
GOOGLE_USERINFO_URL = os.getenv("GOOGLE_USERINFO_URL")
GOOGLE_SCOPES = os.getenv("GOOGLE_SCOPES").split(",")

class GoogleAuthService:
    
    @staticmethod
    def login():
        """Redirect for login google page"""
        
        try:
            params = {
                "client_id": GOOGLE_CLIENT_ID,
                "response_type": "code",
                "scope": " ".join(GOOGLE_SCOPES),
                "redirect_uri": GOOGLE_REDIRECT_URL,
                "access_type": "offline",
                "prompt": "consent"
            }
            logger.info(f"Redirecting to google login: {GOOGLE_AUTH_URL}")
            return RedirectResponse(f"{GOOGLE_AUTH_URL}?{urlencode(params)}")
        except Exception as e:
            logger.error(f"Unexpected error in login(): {e}")
            raise HTTPException(status_code=500, detail="Internal server error")
        
    @staticmethod
    def callback(code:str):
        logger.info("Receive an autorization code and change for a access token")
        
        data = {
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": GOOGLE_REDIRECT_URL
        }
        
        try:
            response = httpx.post(GOOGLE_TOKEN_URL, data=data)
            token_json = response.json()
            
            if "access_token" not in token_json:
                raise HTTPException(status_code=400, detail="Autentication failed")
            
            headers = {"Authorization": f"Bearer {token_json['access_token']}"}
            user_data = httpx.get(GOOGLE_USERINFO_URL, headers=headers).json()
            
            UserService.create_user(user_data)
            
            return {"user_info": user_data, "tokens": token_json}
        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP error during token exchange {e}")
            raise HTTPException(status_code=e.response.status_code, detail="Error during authentication")
        
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise HTTPException(status_code=500, detail="Internal server error")