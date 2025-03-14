import requests
from config.parameters import NEWS_API_KEY
from functools import lru_cache


class NewsAPIClient:
    def __init__(self):
        self.api_key = NEWS_API_KEY
        self.base_url = "https://newsapi.org/v2"

    @lru_cache(maxsize=1)
    def get_instance():
        return NewsAPIClient()

    def fetch_news(self, query: str = None, category: str = None):
        url = f"{self.base_url}/top-headlines"
        params = {
            "apiKey": self.api_key,
            "country": "us",
            "q": query,
            "category": category,
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
