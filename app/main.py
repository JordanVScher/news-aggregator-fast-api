from fastapi import FastAPI
from config.parameters import PYTHON_ENV
from app.routes.news_router import router as news_router
from app.routes.preferences_router import router as preferences_router

app = FastAPI()

app.include_router(news_router)
app.include_router(preferences_router)


@app.get("/")
def root():
    return {"message": f"Welcome to the News Aggregator Api - {PYTHON_ENV}"}


@app.get("/healthcheck")
def healthcheck():
    return "ok"
