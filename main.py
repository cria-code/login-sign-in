from fastapi import FastAPI
from routers.auth_router import router as auth_router

app = FastAPI()

app.include_router(auth_router)

@app.get("/health")
def health_check():
    return ("Health!")

