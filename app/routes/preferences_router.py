from fastapi import APIRouter, Depends
from app.services.preferences_service import PreferencesService
from app.schemas.preferences import (
    PreferencesCreate,
    PreferencesUpdate,
    PreferencesResponse,
)

router = APIRouter(prefix="/api/preferences", tags=["preference", "personal data"])


@router.post("/")
async def create_preferences(
    preferences: PreferencesCreate, preference_service: PreferencesService = Depends()
):
    return await preference_service.create_preferences(preferences)


@router.get("/{user_id}", response_model=PreferencesResponse)
async def get_preferences(
    user_id: str, preference_service: PreferencesService = Depends()
):
    return await preference_service.get_preferences(user_id)


@router.put("/{user_id}")
async def update_preferences(
    user_id: str,
    preferences: PreferencesUpdate,
    preference_service: PreferencesService = Depends(),
):
    return await preference_service.update_preferences(user_id, preferences)


@router.delete("/{user_id}")
async def delete_preferences(
    user_id: str, preference_service: PreferencesService = Depends()
):
    return await preference_service.delete_preferences(user_id)
