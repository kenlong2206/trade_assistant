from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str


class CalculationResponse(BaseModel):
    result: float


@app.post("/calculate")
async def calculate(data: CalculationRequest = Body(...)):
    try:
        if data.operation == "add":
            result = data.num1 + data.num2
        elif data.operation == "subtract":
            result = data.num1 - data.num2
        elif data.operation == "multiply":
            result = data.num1 * data.num2
        elif data.operation == "divide":
            if data.num2 == 0:
                raise ZeroDivisionError("Division by zero")
            result = data.num1 / data.num2
        else:
            raise ValueError("Invalid operation")
        return CalculationResponse(result=result)
    except (ZeroDivisionError, ValueError) as e:
        return {"error": str(e)}
