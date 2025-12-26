from sqlalchemy.orm import Session
from app.models.story import Story
from app.models.enums import Visibility


def create_story(
    db: Session,
    *,
    photo_id: int,
    title: str,
    content: str,
    author_name=None,
    author_relation=None,
    visibility=Visibility.RESTRITA
):
    story = Story(
        photo_id=photo_id,
        title=title,
        content=content,
        author_name=author_name,
        author_relation=author_relation,
        visibility=visibility
    )
    db.add(story)
    db.commit()
    db.refresh(story)
    return story


def list_stories_by_photo(db: Session, photo_id: int):
    return (
        db.query(Story)
        .filter(Story.photo_id == photo_id)
        .order_by(Story.created_at.asc())
        .all()
    )


def list_public_stories_by_photo(db: Session, photo_id: int):
    return (
        db.query(Story)
        .filter(
            Story.photo_id == photo_id,
            Story.visibility == Visibility.PUBLICA
        )
        .order_by(Story.created_at.asc())
        .all()
    )
