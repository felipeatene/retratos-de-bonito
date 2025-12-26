from sqlalchemy.orm import Session
from app.models.photo_person import PhotoPerson
from app.models.person import Person
from app.models.photo import Photo


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


def list_people_by_photo(db: Session, photo_id: int):
    return (
        db.query(
            Person.id,
            Person.full_name,
            Person.nickname,
            Person.birth_year,
            Person.death_year,
            PhotoPerson.role
        )
        .join(PhotoPerson, PhotoPerson.person_id == Person.id)
        .filter(PhotoPerson.photo_id == photo_id)
        .all()
    )


def list_photos_by_person(db: Session, person_id: int):
    return (
        db.query(
            Photo.id,
            Photo.file_name,
            Photo.description,
            Photo.status,
            Photo.visibility,
            PhotoPerson.role,
        )
        .join(PhotoPerson, PhotoPerson.photo_id == Photo.id)
        .filter(PhotoPerson.person_id == person_id)
        .order_by(Photo.created_at.asc())
        .all()
    )
