from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.repositories.public_search_repository import public_search
from app.schemas.public_photo import PublicPhotoResponse

router = APIRouter(prefix="/public", tags=["Busca Pública"]) 


@router.get("/search", response_model=list[PublicPhotoResponse])
def search_public_photos(
    text: str | None = None,
    person: str | None = None,
    year: int | None = None,
    location: str | None = None,
    db: Session = Depends(get_db)
):
    photos = public_search(
        db,
        text=text,
        person_name=person,
        year=year,
        location_name=location
    )

    return [
        PublicPhotoResponse(
            photo_id=p.id,
            file_name=p.file_name,
            description=p.description,
            original_date=p.original_date,
            location=p.location.name if p.location else None
        )
        for p in photos
    ]
