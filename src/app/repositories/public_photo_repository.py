from sqlalchemy.orm import Session
from app.models.photo import Photo
from app.models.photo_person import PhotoPerson
from app.models.person import Person
from app.models.location import Location
from app.models.enums import PhotoStatus, Visibility
from app.models.enums import ConsentType
from app.models.consent import Consent


def get_public_photo_detail(db: Session, photo_id: int):
    photo = (
        db.query(Photo)
        .filter(
            Photo.id == photo_id,
            Photo.status == PhotoStatus.VALIDADA,
            Photo.visibility == Visibility.PUBLICA,
        )
        .first()
    )

    if not photo:
        return None

    people = (
        db.query(
            Person.full_name,
            Person.nickname,
            Person.birth_year,
            Person.death_year,
            PhotoPerson.role,
        )
        .join(PhotoPerson, PhotoPerson.person_id == Person.id)
        .outerjoin(
            Consent,
            (Consent.photo_id == photo.id) & (Consent.person_id == Person.id),
        )
        .filter(
            (Consent.consent_type == ConsentType.PUBLICO) | (Consent.id.is_(None))
        )
        .all()
    )

    return photo, people
