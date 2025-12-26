from pydantic import BaseModel
from typing import Optional


class ExpoPhotoResponse(BaseModel):
    photo_id: int
    file_name: str
    description: Optional[str] = None
    decade: Optional[int] = None
    location: Optional[str] = None
