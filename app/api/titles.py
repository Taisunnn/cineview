from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select, func

from app.core.database import get_db
from app.api.auth import get_current_user
import app.core.exceptions as exceptions
import app.schemas as schemas
import app.models as models

router = APIRouter()


@router.get("/")
async def read_titles(
    current_user: Annotated[dict, Depends(get_current_user)], db=Depends(get_db)
):
    titles = await db.execute(select(models.Titles))
    return titles.scalars().all()


@router.get("/id/{title_id}", response_model=list[schemas.Titles])
async def get_title(
    title_id: int,
    current_user: Annotated[dict, Depends(get_current_user)],
    db=Depends(get_db),
):
    title = (
        await db.execute(
            select(models.Titles).where(models.Titles.title_id == title_id)
        )
    ).one_or_none()
    if not title:
        raise exceptions.get_not_found_exception("Title not found")
    return title


@router.get("/name/{title_name}", response_model=list[schemas.Titles])
async def get_title_name(
    title_name: str,
    current_user: Annotated[dict, Depends(get_current_user)],
    db=Depends(get_db),
):
    title = (
        await db.execute(
            select(models.Titles).where(
                func.lower(models.Titles.title_name).ilike(f"%{title_name}%")
            )
        )
    ).first()
    if not title:
        raise exceptions.get_not_found_exception("Title not found")
    return title
