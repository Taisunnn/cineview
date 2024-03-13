import pytest


@pytest.mark.asyncio
async def test_main(async_app_client):
    response = await async_app_client.get("/health")
    assert response.status_code == 200
    assert len(response.json()) == 1
