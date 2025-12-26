from pydantic import BaseModel
from typing import Optional


class PublicPhotoResponse(BaseModel):
    photo_id: int
    file_name: str
    description: Optional[str] = None
    original_date: Optional[str] = None
    location: Optional[str] = None
