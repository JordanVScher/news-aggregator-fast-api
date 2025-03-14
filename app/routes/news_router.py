from fastapi import APIRouter, Depends
from app.services.news_service import NewsService

router = APIRouter(prefix="/api/news", tags=["news"])


@router.get("/")
def get_news(
    query: str = None, category: str = None, news_service: NewsService = Depends()
):
    """
    Fetch news articles based on a query or category
    """
    return news_service.fetch_news(query, category)
