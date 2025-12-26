from sqlalchemy.orm import Session
from app.models.photo_person import PhotoPerson


def link_exists(db: Session, photo_id: int, person_id: int) -> bool:
    return (
        db.query(PhotoPerson)
        .filter(
            PhotoPerson.photo_id == photo_id,
            PhotoPerson.person_id == person_id
        )
        .first()
        is not None
    )


def link_person_to_photo(
    db: Session,
    *,
    photo_id: int,
    person_id: int,
    role: str
):
    link = PhotoPerson(
        photo_id=photo_id,
        person_id=person_id,
        role=role
    )
    db.add(link)
    db.commit()
    db.refresh(link)
    return link
