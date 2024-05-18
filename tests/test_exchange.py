import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app

@pytest.mark.asyncio
async def test_message():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/message", json={"Name": "Alice", "Age": 30})
    assert response.status_code == 200
    assert response.json() == {"message": "your name is Alice and your age is 30"}

@pytest.mark.asyncio
async def test_calculate_add():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/calculate", json={"num1": 1, "num2": 2, "operation": "add"})
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

@pytest.mark.asyncio
async def test_calculate_subtract():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/calculate", json={"num1": 5, "num2": 3, "operation": "subtract"})
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}

@pytest.mark.asyncio
async def test_calculate_multiply():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/calculate", json={"num1": 2, "num2": 3, "operation": "multiply"})
    assert response.status_code == 200
    assert response.json() == {"result": 6.0}

@pytest.mark.asyncio
async def test_calculate_divide():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/calculate", json={"num1": 10, "num2": 2, "operation": "divide"})
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

@pytest.mark.asyncio
async def test_calculate_divide_by_zero():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/calculate", json={"num1": 10, "num2": 0, "operation": "divide"})
    assert response.status_code == 200
    assert response.json() == {"error": "Division by zero"}

@pytest.mark.asyncio
async def test_calculate_invalid_operation():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/calculate", json={"num1": 10, "num2": 2, "operation": "invalid"})
    assert response.status_code == 200
    assert response.json() == {"error": "Invalid operation"}
