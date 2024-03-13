import pytest_asyncio
from httpx import AsyncClient

from main import app

pytest_plugins = ("pytest_asyncio",)


@pytest_asyncio.fixture(scope="session", autouse=True)
async def async_app_client():
    async with AsyncClient(app=app, base_url="http://localhost") as client:
        yield client
