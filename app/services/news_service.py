import requests
from fastapi import HTTPException
from app.services.news_api_client import NewsAPIClient
import json


class NewsService:
    def __init__(self):
        self.news_api_client = NewsAPIClient.get_instance()

    def fetch_news(self, query: str = None, category: str = None):
        try:
            news = self.news_api_client.fetch_news(query, category)
            return news
        except requests.exceptions.RequestException as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to fetch news: {str(e)}"
            )
