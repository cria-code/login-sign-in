from configs.log_config import logger
from fastapi import APIRouter, HTTPException
from services.auth_service import GoogleAuthService

router = APIRouter()

@router.get("/auth/login")
def login():
    """Start the flow of routes, redirecting to google auth"""
    try:
        logger.info("login endpoint hit")
        return GoogleAuthService.login()
    except Exception as e:
        logger.error(f"Error in login route: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    
@router.get("/auth/callback")
def callback(code: str):
    """Process the answer of google auth and save user"""
    try:
        logger.info("Callback endpoint hit with code")
        return GoogleAuthService.callback(code)
    except Exception as e:
        logger.error(f"Error in callback route: {e}")
        raise HTTPException(status_code=400, detail=str(e))