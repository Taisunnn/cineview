import pytest


@pytest.mark.asyncio
async def test_get_title_no_auth(async_app_client):
    response = await async_app_client.get("/titles/id/1")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_title(async_app_client, access_token):
    response = await async_app_client.get("/titles/id/1", headers=access_token)
    assert response.status_code == 200
    assert len(response.json()) == 1
