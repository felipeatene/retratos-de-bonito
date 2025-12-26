from pydantic import BaseModel
from typing import Optional, List


class PublicPhotoPerson(BaseModel):
    full_name: str
    nickname: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None
    role: str


class PublicPhotoDetailResponse(BaseModel):
    photo_id: int
    file_name: str
    description: Optional[str] = None
    original_date: Optional[str] = None
    decade: Optional[int] = None
    location: Optional[str] = None
    source: Optional[str] = None
    people: List[PublicPhotoPerson]
