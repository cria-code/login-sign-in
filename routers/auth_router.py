from fastapi import APIRouter
from services.auth_service import GoogleAuthService

router = APIRouter()

@router.get("/auth/login")
def login():
    """Start the flow of routes, directing to google auth"""
    return GoogleAuthService.login()

@router.get("/auth/callback")
def callback(code: str):
    """Process the answer of google auth and save user"""
    return GoogleAuthService.callback(code)