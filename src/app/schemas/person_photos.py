from pydantic import BaseModel
from typing import Optional
from app.models.enums import PhotoStatus, Visibility


class PersonPhotoResponse(BaseModel):
    photo_id: int
    file_name: str
    description: Optional[str] = None
    status: PhotoStatus
    visibility: Visibility
    role: str
