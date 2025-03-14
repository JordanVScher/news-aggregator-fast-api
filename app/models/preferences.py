from pydantic import BaseModel
from typing import List


class UserPreferences(BaseModel):
    user_id: str
    categories: List[str]
    sources: List[str]

    class Config:
        schema_extra = {
            "example": {
                "user_id": "123",
                "categories": ["technology", "literature"],
                "sources": ["bbc-news", "cnn"],
            }
        }
