from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.photo import Photo
from app.models.person import Person
from app.models.photo_person import PhotoPerson
from app.models.location import Location
from app.models.enums import PhotoStatus, Visibility


def public_search(
    db: Session,
    *,
    text: str | None = None,
    person_name: str | None = None,
    year: int | None = None,
    location_name: str | None = None
):
    query = (
        db.query(Photo)
        .filter(
            Photo.status == PhotoStatus.VALIDADA,
            Photo.visibility == Visibility.PUBLICA
        )
    )

    if text:
        query = query.filter(Photo.description.ilike(f"%{text}%"))

    if year:
        query = query.filter(Photo.original_date.ilike(f"%{year}%"))

    if location_name:
        query = (
            query.join(Location, isouter=True)
            .filter(Location.name.ilike(f"%{location_name}%"))
        )

    if person_name:
        query = (
            query.join(PhotoPerson)
            .join(Person)
            .filter(Person.full_name.ilike(f"%{person_name}%"))
        )

    return query.order_by(Photo.created_at.asc()).all()
