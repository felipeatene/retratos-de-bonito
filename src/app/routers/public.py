from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.repositories.public_search_repository import public_search
from app.schemas.public_photo import PublicPhotoResponse
from app.repositories.timeline_repository import timeline_by_decade
from app.schemas.timeline import TimelineDecade, TimelinePhoto
from app.repositories.public_photo_repository import get_public_photo_detail
from app.schemas.public_photo_detail import (
    PublicPhotoDetailResponse,
    PublicPhotoPerson,
)

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


@router.get("/timeline", response_model=list[TimelineDecade])
def get_public_timeline(db: Session = Depends(get_db)):
    timeline = timeline_by_decade(db)

    response: list[TimelineDecade] = []

    for decade in sorted(timeline.keys()):
        response.append(
            TimelineDecade(
                decade=decade,
                photos=[
                    TimelinePhoto(
                        photo_id=p.id,
                        file_name=p.file_name,
                        description=p.description,
                        original_date=p.original_date
                    )
                    for p in timeline[decade]
                ]
            )
        )

    return response


@router.get("/photos/{photo_id}", response_model=PublicPhotoDetailResponse)
def get_public_photo(photo_id: int, db: Session = Depends(get_db)):
    result = get_public_photo_detail(db, photo_id)

    if not result:
        raise HTTPException(status_code=404, detail="Foto não encontrada")

    photo, people = result

    decade = None
    if photo.original_date:
        try:
            year = int(photo.original_date[:4])
            decade = (year // 10) * 10
        except ValueError:
            pass

    return PublicPhotoDetailResponse(
        photo_id=photo.id,
        file_name=photo.file_name,
        description=photo.description,
        original_date=photo.original_date,
        decade=decade,
        location=photo.location.name if photo.location else None,
        source=photo.source,
        people=[
            PublicPhotoPerson(
                full_name=p.full_name,
                nickname=p.nickname,
                birth_year=p.birth_year,
                death_year=p.death_year,
                role=p.role,
            )
            for p in people
        ],
    )
