from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.services.photo_storage import calculate_hash, save_photo_file
from app.repositories.photo_repository import get_by_hash, create_photo
from app.schemas.person_link import LinkPersonToPhotoRequest
from app.services.person_link_service import add_person_to_photo
from app.schemas.photo_curation import CuratePhotoRequest
from app.repositories.photo_repository import update_photo_curation
from app.models.photo import Photo
from app.repositories.photo_person_repository import list_people_by_photo
from app.schemas.photo_people import PhotoPersonResponse

router = APIRouter(prefix="/photos", tags=["Fotos"])

@router.post("/upload")
async def upload_photo(
    file: UploadFile = File(...),
    description: str | None = None,
    source: str | None = None,
    collection_id: int | None = None,
    db: Session = Depends(get_db)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Arquivo não é uma imagem")
    file_hash = calculate_hash(file)
    existing = get_by_hash(db, file_hash)
    if existing:
        raise HTTPException(
            status_code=409,
            detail="Esta foto já existe no acervo"
        )
    file_name, file_path = save_photo_file(file)
    photo = create_photo(
        db,
        file_name=file_name,
        file_path=file_path,
        file_hash=file_hash,
        description=description,
        source=source,
        collection_id=collection_id
    )
    return {
        "id": photo.id,
        "status": "upload_realizado",
        "photo_status": photo.status,
        "visibility": photo.visibility
    }


@router.post("/{photo_id}/people")
def add_person(
    photo_id: int,
    payload: LinkPersonToPhotoRequest,
    db: Session = Depends(get_db)
):
    # delega toda a lógica ao serviço
    return add_person_to_photo(db, photo_id, payload)


@router.patch("/{photo_id}/curate")
def curate_photo(
    photo_id: int,
    payload: CuratePhotoRequest,
    db: Session = Depends(get_db)
):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()
    if not photo:
        raise HTTPException(status_code=404, detail="Foto não encontrada")

    if not payload.status and not payload.visibility:
        raise HTTPException(
            status_code=400,
            detail="Nenhuma alteração de curadoria informada"
        )

    photo = update_photo_curation(
        db,
        photo=photo,
        status=payload.status,
        visibility=payload.visibility,
        curator_name=payload.curator_name
    )

    return {
        "photo_id": photo.id,
        "status": photo.status,
        "visibility": photo.visibility,
        "curated": True
    }


@router.get("/{photo_id}/people", response_model=list[PhotoPersonResponse])
def get_people_from_photo(
    photo_id: int,
    db: Session = Depends(get_db)
):
    photo = db.query(Photo).filter(Photo.id == photo_id).first()
    if not photo:
        raise HTTPException(status_code=404, detail="Foto não encontrada")

    people = list_people_by_photo(db, photo_id)

    return [
        PhotoPersonResponse(
            person_id=p.id,
            full_name=p.full_name,
            nickname=p.nickname,
            birth_year=p.birth_year,
            death_year=p.death_year,
            role=p.role
        )
        for p in people
    ]
