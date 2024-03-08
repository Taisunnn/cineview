from fastapi import APIRouter

import app.api.auth as auth
import app.api.users as users
import app.api.titles as titles

router = APIRouter()

router.include_router(auth.router, tags=["auth"], prefix="/auth")
router.include_router(users.router, tags=["users"], prefix="/user")
router.include_router(titles.router, tags=["titles"], prefix="/titles")