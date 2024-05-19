import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app

@pytest.mark.asyncio
async def test_exchange_binance():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/exchange/exchange", json={"Exchange": "Binance"})
    assert response.status_code == 200
    assert response.json() == {"TradeResult": "Success"}

@pytest.mark.asyncio
async def test_exchange_kucoin():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/exchange/exchange", json={"Exchange": "Kucoin"})
    assert response.status_code == 200
    assert response.json() == {"TradeResult": "Invalid Exchange"}

@pytest.mark.asyncio
async def test_exchange_empty():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/exchange/exchange", json={"Exchange": ""})
    assert response.status_code == 200
    assert response.json() == {"TradeResult": "Invalid Request"}

@pytest.mark.asyncio
async def test_exchange_invalid():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/exchange/exchange", json={"Exchange": ""})
    assert response.status_code == 200
    assert response.json() == {"TradeResult": "Invalid Request"}
