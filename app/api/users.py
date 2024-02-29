from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from app.core.database import get_db
from app.api.auth import get_current_user
import app.core.exceptions as exceptions
import app.schemas as schemas
import app.models as models

router = APIRouter()


@router.get("/")
async def read_users(current_user: Annotated[dict, Depends(get_current_user)],
    db=Depends(get_db)
):
    users = (await db.execute(select(models.Users)))
    return users.scalar()


@router.get("/{user_id}", response_model=list[schemas.Users])
async def get_user(user_id: int,
    current_user: Annotated[dict, Depends(get_current_user)],
    db=Depends(get_db)
):
    user = (await db.execute(select(models.Users).where(models.Users.user_id == user_id))).one_or_none()
    if not user:
        raise exceptions.get_not_found_exception("User not found")
    return user