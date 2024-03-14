from datetime import timedelta, datetime
from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt, JWTError

from app.core.settings import Settings
from app.core.database import get_db
import app.core.exceptions as exceptions
import app.models as models
import app.schemas as schemas

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

db_dependency = Annotated[Session, Depends(get_db)]


async def authenticate_user(username: str, password: str, db: db_dependency):
    record = select(models.Login).where(models.Login.username == username)
    result = await db.execute(record)
    user = result.scalar_one_or_none()
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, login_id: int, expires_delta: timedelta):
    encode = {"sub": username, "id": login_id}
    expires = datetime.utcnow() + expires_delta
    encode.update({"exp": expires})
    return jwt.encode(encode, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM)


async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(
            token, Settings.SECRET_KEY, algorithms=[Settings.ALGORITHM]
        )
        username: str = payload.get("sub")
        login_id: int = payload.get("id")
        if username is None or login_id is None:
            raise exceptions.get_unauthorized_exception()
        return {"username": username, "id": login_id}
    except JWTError:
        raise exceptions.get_unauthorized_exception()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    create_user_request: schemas.CreateUserRequest, db: db_dependency
):
    create_user_model = models.Login(
        username=create_user_request.username,
        hashed_password=pwd_context.hash(create_user_request.password),
    )
    db.add(create_user_model)
    await db.commit()


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    user = await authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise exceptions.get_unauthorized_exception()
    token = create_access_token(user.username, user.login_id, timedelta(minutes=20))

    return {"access_token": token, "token_type": "bearer"}
