from datetime import timedelta

import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy import text

from main import app
from app.core.database import SessionLocal
from app.api.auth import create_access_token
import app.models as models

pytest_plugins = ("pytest_asyncio",)


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database():
    async with SessionLocal() as db:
        db.add(
            models.Titles(
                title_id=1,
                title_name="test_movie",
                score=9.8,
                synopsis="this is the synopsis",
                episodes=1,
            )
        )
        await db.commit()
        yield
        await db.execute(text("TRUNCATE TABLE titles"))


@pytest_asyncio.fixture(scope="session")
async def async_app_client():
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        yield client


@pytest_asyncio.fixture()
async def access_token():
    token = create_access_token(
        username="testuser", login_id=1, expires_delta=timedelta(minutes=30)
    )

    return {"Authorization": f"Bearer {token}"}
