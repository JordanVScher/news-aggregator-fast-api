from fastapi import FastAPI
from config.parameters import PYTHON_ENV

app = FastAPI()


@app.get("/")
def root():
    return {"message": f"Welcome to the News Aggregator Api - {PYTHON_ENV}"}


@app.get("/healthcheck")
async def healthcheck():
    return "ok"
