from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

class CalculationRequest(BaseModel):
  num1: float
  num2: float
  operation: str

class CalculationResponse(BaseModel):
  result: float

class MessageFields(BaseModel):
    Name: str
    Age: int

class MessageResponse(BaseModel):
    message: str

@app.post("/message")
async def message(data: MessageFields = Body(...)):
    message = "your name is " + data.Name + " and your age is " + str(data.Age)
    return MessageResponse (message=message)

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

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("trade_assistant.main:app", host="127.0.0.1", port=8000)
