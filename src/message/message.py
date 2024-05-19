from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class MessageFields(BaseModel):
    Name: str
    Age: int


class MessageResponse(BaseModel):
    message: str


@app.post("/message")
async def message(data: MessageFields = Body(...)):
    msg = "your name is " + data.Name + " and your age is " + str(data.Age)
    return MessageResponse(message=msg)
