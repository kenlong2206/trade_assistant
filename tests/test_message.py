import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app

@pytest.mark.asyncio
async def test_message():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/message", json={"Name": "Alice", "Age": 30})
    assert response.status_code == 200
    assert response.json() == {"message": "your name is Alice and your age is 30"}


