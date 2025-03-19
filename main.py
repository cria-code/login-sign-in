"""
This module handles the initialisation of FastApi
"""
from fastapi import FastAPI
from routers.user_router import router
import logging

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)


@app.get("/health")
def health_check():
    """
    Healthy check to see if the application is working in a basic way
    """
    return ("Health!")


app.include_router(router)
