"""
This module handles authentication routes using Google OAuth.
"""
import os
import logging
from typing import Annotated
from fastapi import APIRouter, Request, Depends, HTTPException
from services.auth_service import AuthService
from storages.user_storage import UserStorage
from configs.db_conn import get_database

router = APIRouter()
logger = logging.getLogger(__name__)
storage = UserStorage(db_connection=get_database())

REDIRECT_URL = "http://localhost:8000/auth/google/callback"


def get_auth_service() -> AuthService:
    """
    Retrieves an instance of the authentication service.
    """
    return AuthService()


ServiceDep = Annotated[AuthService, Depends(get_auth_service)]


@router.get("/auth/google")
def login() -> dict:
    """
    Generates and returns the Google OAuth login URL.
    """
    login_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth"
        f"?client_id={os.getenv('GOOGLE_CLIENT_ID')}"
        f"&redirect_uri={REDIRECT_URL}"
        f"&response_type=code"
        f"&scope=openid%20email%20profile"
        f"&access_type=offline"
        f"&prompt=consent"
    )

    logger.info("Google Login URL generated successfully.")
    return {"login_url": login_url}


@router.get("/auth/google/callback")
def callback(request: Request, service: ServiceDep) -> dict:
    """
    Handles the Google OAuth callback, exchanges the code for an access token,
    retrieves user information, and saves it to the database.
    """
    code = request.query_params.get("code")
    if not code:
        logger.error("Authentication code not found in request.")
        raise HTTPException(status_code=400, detail="Code not found")
    try:
        logger.info("Starting authentication with Google...")
        user_data = service.authenticate_user(code, REDIRECT_URL)
        storage.save_user(user_data)
        logger.info("User authenticated and saved successfully.")

        return {"message": "Login Successfully!", "user": user_data}

    except Exception as ex:
        logger.error(f"Error during authentication: {ex}")
        raise HTTPException(
            status_code=500, detail="Error authenticating user.")
