"""
Module for handling authentication via Google OAuth.
"""
import os
import httpx
import logging
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()


class AuthService:
    """
    This class manages authentication using Google OAuth.
    """
    def __init__(self, http_client=httpx):
        self.logger = logging.getLogger(__name__)
        self.http_client = http_client
        self.google_client_id = os.getenv("GOOGLE_CLIENT_ID")
        self.google_client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
        self.token_url = "https://oauth2.googleapis.com/token"
        self.user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"

    def get_access_token(self, code: str, redirect_url: str) -> str:
        """
        Exchanges an authorization code for an access token.
        """
        self.logger.info("Receiving OAuth code and requesting token...")

        response = self.http_client.post(
            self.token_url,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "client_id": self.google_client_id,
                "client_secret": self.google_client_secret,
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": redirect_url
            }
        )

        if response.status_code != 200:
            self.logger.error("Error getting token: %s", response.text)
            raise HTTPException(
                status_code=400, detail="Error getting the token")

        access_token = response.json().get("access_token")
        self.logger.info("Access Token successfully obtained.")
        return access_token

    def get_user_info(self, access_token: str) -> dict:
        """
        Fetches user information using an access token.
        """
        self.logger.info("Fetching user information...")

        response = self.http_client.get(
            self.user_info_url,
            headers={"Authorization": f"Bearer {access_token}"}
        )

        if response.status_code != 200:
            self.logger.error("Error getting user data: %s", response.text)
            raise HTTPException(
                status_code=400, detail="Error getting user data")

        self.logger.info("User data successfully obtained.")
        return response.json()

    def authenticate_user(self, code: str, redirect_url: str) -> dict:
        """
        Authenticates a user by obtaining an access token.
        """
        access_token = self.get_access_token(code, redirect_url)
        return self.get_user_info(access_token)
