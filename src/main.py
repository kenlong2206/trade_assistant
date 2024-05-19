from fastapi import FastAPI
from src.message.message import app as messages_app
from src.calculator.calculator import app as calculator_app
from src.exchange.exchange import app as exchange_app

app = FastAPI()


# now mount the apps
app.mount("/message", messages_app)
app.mount("/calculator", calculator_app)
app.mount("/exchange", exchange_app)

# start function created just to make it easier to run a unit test against it (otherwise the application needs to ebe run which isnt normally part of unit testing)
def start():
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000)

if __name__ == "__main__":
    start()
