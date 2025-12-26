from pydantic import BaseModel
from typing import Optional
from app.models.enums import Visibility


class CreateStoryRequest(BaseModel):
    title: str
    content: str
    author_name: Optional[str] = None
    author_relation: Optional[str] = None
    visibility: Visibility = Visibility.RESTRITA


class StoryResponse(BaseModel):
    id: int
    title: str
    content: str
    author_name: Optional[str]
    author_relation: Optional[str]
    visibility: Visibility
