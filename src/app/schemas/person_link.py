from pydantic import BaseModel
from typing import Optional


class LinkPersonToPhotoRequest(BaseModel):
    full_name: str
    nickname: Optional[str] = None
    birth_year: Optional[int] = None
    death_year: Optional[int] = None
    role: str = "retratado"
