import time

from fastapi import FastAPI, Request
from app.core.middleware import log_request_time

from app.api import users
from app.api import auth

app = FastAPI()

app.middleware("http")(log_request_time)

@app.get("/health")
async def healthcheck():
    return {"status": "healthy"}

app.include_router(auth.router, tags=["auth"], prefix="/auth")
app.include_router(users.router, tags=["users"], prefix="/user")