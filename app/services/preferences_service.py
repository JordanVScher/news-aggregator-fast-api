from fastapi import HTTPException, Depends
from app.models.preferences import UserPreferences
from app.schemas.preferences import (
    PreferencesCreate,
    PreferencesUpdate,
    PreferencesResponse,
)
from app.utils.mongo_client import MongoClientSingleton, get_mongo_client
from bson import ObjectId


class PreferencesService:
    def __init__(self, mongo_client: MongoClientSingleton = Depends(get_mongo_client)):
        self.mongo_client = mongo_client
        self.collection = self.mongo_client.get_sync_db()["user_preferences"]

    async def create_preferences(self, preferences: PreferencesCreate):
        """
        Create a new user preferences document
        """
        preferences_data = preferences.model_dump()
        user_id = preferences_data["user_id"]

        preferences_found = self.collection.find_one({"user_id": user_id})
        if preferences_found:
            raise HTTPException(
                status_code=403, detail="Preferences for this user already exists"
            )

        result = self.collection.insert_one(preferences_data)

        if not result.inserted_id:
            raise HTTPException(status_code=500, detail="Failed to create preferences")
        return {"id": str(result.inserted_id)}

    async def get_preferences(self, user_id: str):
        """
        Get user preferences by user_id
        """
        preferences = self.collection.find_one({"user_id": user_id})
        if not preferences:
            raise HTTPException(status_code=404, detail="Preferences not found")
        return PreferencesResponse(**preferences)

    async def update_preferences(self, user_id: str, preferences: PreferencesUpdate):
        """
        Update user preferences by user_id
        """
        preferences_data = {
            k: v for k, v in preferences.model_dump().items() if v is not None
        }
        result = self.collection.update_one(
            {"user_id": user_id}, {"$set": preferences_data}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Preferences not found")
        return {"message": "Preferences updated successfully"}

    async def delete_preferences(self, user_id: str):
        """
        Delete user preferences by user_id
        """
        result = self.collection.delete_one({"user_id": user_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Preferences not found")
        return {"message": "Preferences deleted successfully"}
