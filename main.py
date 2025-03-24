import logging
from fastapi import FastAPI
from routers.auth_router import router as auth_router

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

app.include_router(auth_router)

@app.get("/health")
def health_check():
    return ("Health!")

