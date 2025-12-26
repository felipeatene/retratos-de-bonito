from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.schemas.consent import CreateConsentRequest
from app.repositories.consent_repository import (
    create_or_update_consent,
    get_consent,
)
from app.models.photo import Photo
from app.models.person import Person

router = APIRouter(prefix="/consents", tags=["Consentimento"])


@router.post("/photos/{photo_id}/people/{person_id}")
def set_consent(
    photo_id: int,
    person_id: int,
    payload: CreateConsentRequest,
    db: Session = Depends(get_db)
):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()
    if not photo:
        raise HTTPException(status_code=404, detail="Foto não encontrada")

    person = db.query(Person).filter(Person.id == person_id).first()
    if not person:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada")

    consent = create_or_update_consent(
        db,
        photo_id=photo_id,
        person_id=person_id,
        consent_type=payload.consent_type,
        consent_date=payload.consent_date,
        notes=payload.notes,
    )

    return {
        "photo_id": photo_id,
        "person_id": person_id,
        "consent_type": consent.consent_type,
        "status": "consentimento_registrado",
    }


@router.get("/photos/{photo_id}/people/{person_id}")
def get_person_consent(
    photo_id: int,
    person_id: int,
    db: Session = Depends(get_db)
):
    consent = get_consent(db, photo_id=photo_id, person_id=person_id)

    if not consent:
        return {
            "photo_id": photo_id,
            "person_id": person_id,
            "consent": "nao_registrado",
        }

    return {
        "photo_id": photo_id,
        "person_id": person_id,
        "consent_type": consent.consent_type,
        "consent_date": consent.consent_date,
        "notes": consent.notes,
    }
