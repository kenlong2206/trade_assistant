import pytest
from httpx import AsyncClient, ASGITransport
from src.main import app

@pytest.mark.asyncio
async def test_exchange():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="https://test") as ac:
        response = await ac.post("/exchange/exchange", json={"Exchange": "Binance"})
    assert response.status_code == 200
    assert response.json() == {"TradeResult": "Success"}



