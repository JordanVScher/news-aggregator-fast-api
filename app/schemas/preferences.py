from pydantic import BaseModel, Field, ConfigDict
from pydantic.functional_validators import BeforeValidator
from bson import ObjectId
from typing import Annotated, List, Optional

PyOjectId = Annotated[
    str, BeforeValidator(lambda x: str(x) if ObjectId.is_valid(x) else None)
]


class PreferencesResponse(BaseModel):
    id: PyOjectId = Field(alias="_id")
    user_id: str
    categories: List[str]
    sources: List[str]

    model_config = ConfigDict(
        allow_population_by_field_name=True, json_encoders={ObjectId: str}
    )


class PreferencesCreate(BaseModel):
    user_id: str
    categories: List[str]
    sources: List[str]


class PreferencesUpdate(BaseModel):
    categories: Optional[List[str]]
    sources: Optional[List[str]]
