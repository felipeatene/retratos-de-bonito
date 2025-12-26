from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.repositories.photo_person_repository import list_photos_by_person
from app.models.person import Person
from app.schemas.person_photos import PersonPhotoResponse

router = APIRouter(prefix="/people", tags=["Pessoas"])


@router.get("/{person_id}/photos", response_model=list[PersonPhotoResponse])
def get_photos_by_person(
    person_id: int,
    db: Session = Depends(get_db)
):
    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    photos = list_photos_by_person(db, person_id)

    return [
        PersonPhotoResponse(
            photo_id=p.id,
            file_name=p.file_name,
            description=p.description,
            status=p.status,
            visibility=p.visibility,
            role=p.role
        )
        for p in photos
    ]
