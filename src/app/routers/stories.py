from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.schemas.story import CreateStoryRequest, StoryResponse
from app.repositories.story_repository import (
    create_story,
    list_stories_by_photo,
    list_public_stories_by_photo,
)
from app.models.photo import Photo

router = APIRouter(prefix="/stories", tags=["Histórias"])


@router.post("/photos/{photo_id}", response_model=StoryResponse)
def add_story_to_photo(
    photo_id: int,
    payload: CreateStoryRequest,
    db: Session = Depends(get_db)
):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()
    if not photo:
        raise HTTPException(status_code=404, detail="Foto não encontrada")

    story = create_story(
        db,
        photo_id=photo_id,
        title=payload.title,
        content=payload.content,
        author_name=payload.author_name,
        author_relation=payload.author_relation,
        visibility=payload.visibility,
    )

    return story


@router.get("/photos/{photo_id}", response_model=list[StoryResponse])
def get_stories_of_photo(
    photo_id: int,
    db: Session = Depends(get_db)
):
    return list_stories_by_photo(db, photo_id)
