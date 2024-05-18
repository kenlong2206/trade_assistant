from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class OpenPositionRequest(BaseModel):
    assetPair: str
    exchange: str
    position: str
    tradeEntry: float
    tradeStopLoss: float
    tradeTakeProfit: float
    tradeSize: float
    tradeLeverage: float


class OpenPositionResponse(BaseModel):
    tradeResult: str


@app.post("/exchange")
async def exchange(data: OpenPositionRequest = Body(...)):
    if data.exchange == "Binance":
        result = "Success"
    elif data.exchange == "Kucoin":
        result = "Invalid Exchange"
    else:
        result = "Invalid Request"
    return OpenPositionResponse(tradeResult=result)
