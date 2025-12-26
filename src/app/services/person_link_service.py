from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.person_repository import get_by_name, create_person
from app.repositories.photo_person_repository import link_exists, link_person_to_photo
from app.models.photo import Photo


def add_person_to_photo(db: Session, photo_id: int, payload) -> dict:
    # valida foto
    photo = db.query(Photo).filter(Photo.id == photo_id).first()
    if not photo:
        raise HTTPException(status_code=404, detail="Foto não encontrada")

    # pessoa (get or create)
    person = get_by_name(db, payload.full_name)
    if not person:
        person = create_person(
            db,
            full_name=payload.full_name,
            nickname=payload.nickname,
            birth_year=payload.birth_year,
            death_year=payload.death_year
        )

    # evita duplicidade
    if link_exists(db, photo_id, person.id):
        raise HTTPException(
            status_code=409,
            detail="Pessoa já vinculada a esta foto"
        )

    link = link_person_to_photo(
        db,
        photo_id=photo_id,
        person_id=person.id,
        role=payload.role
    )

    return {
        "photo_id": photo_id,
        "person_id": person.id,
        "full_name": person.full_name,
        "role": payload.role,
        "status": "vinculo_criado"
    }
