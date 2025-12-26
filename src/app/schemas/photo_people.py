from pydantic import BaseModel
from typing import Optional


class PhotoPersonResponse(BaseModel):
    person_id: int
    full_name: str
    nickname: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None
    role: str
