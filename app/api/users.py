from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from app.core.database import get_db
import app.schemas as schemas
import app.models as models

router = APIRouter()

@router.get("/")
async def read_users():
    return {"User": "Page"}

@router.get("/{user_id}", response_model=list[schemas.Users])
async def get_user(user_id: int, db=Depends(get_db)):
    user = (await db.execute(select(models.Users).where(models.Users.user_id == user_id))).one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user