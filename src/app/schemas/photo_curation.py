from pydantic import BaseModel
from typing import Optional
from app.models.enums import PhotoStatus, Visibility


class CuratePhotoRequest(BaseModel):
    status: Optional[PhotoStatus] = None
    visibility: Optional[Visibility] = None
    curator_name: Optional[str] = None
