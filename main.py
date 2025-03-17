from fastapi import FastAPI
from routers.user_router import router
import logging

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)


@app.get("/health")
def health_check():
    return ("Health!")


app.include_router(router)
