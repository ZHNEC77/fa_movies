from datetime import date
from fastapi_jsonapi.schema_base import BaseModel


class MovieAttributesSchema(BaseModel):
    title: str
    description: str
    release_date: date | None = None
    duration: int | None = None
