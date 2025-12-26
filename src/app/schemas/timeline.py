from pydantic import BaseModel
from typing import Optional, List


class TimelinePhoto(BaseModel):
    photo_id: int
    file_name: str
    description: Optional[str] = None
    original_date: Optional[str] = None


class TimelineDecade(BaseModel):
    decade: int
    photos: List[TimelinePhoto]
