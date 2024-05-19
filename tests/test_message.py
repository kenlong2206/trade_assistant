import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app

@pytest.mark.asyncio
async def test_message1():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/message/message", json={"Name": "Alice", "Age": 30})
    assert response.status_code == 200
    assert response.json() == {"message": "your name is Alice and your age is 30"}

@pytest.mark.asyncio
async def test_message2():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/message/message", json={"Name": "Barry", "Age": -1})
    assert response.status_code == 200
    assert response.json() == {"message": "your name is Barry and your age is -1"}


@pytest.mark.asyncio
async def test_message3():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/message/message", json={"Name": "Fred", "Age": 123})
    assert response.status_code == 200
    assert response.json() == {"message": "your name is Fred and your age is 123"}
