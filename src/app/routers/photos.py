from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from app.dependencies.db import get_db
from app.dependencies.auth import get_current_user, get_optional_current_user, get_curator_user
from app.services.photo_storage import calculate_hash, save_photo_file
from app.repositories.photo_repository import (
    get_by_hash, 
    create_photo, 
    update_photo_curation,
    list_photos_by_contributor
)
from app.schemas.person_link import LinkPersonToPhotoRequest
from app.services.person_link_service import add_person_to_photo
from app.schemas.photo_curation import CuratePhotoRequest
from app.models.photo import Photo
from app.models.user import User
from app.repositories.photo_person_repository import list_people_by_photo
from app.schemas.photo_people import PhotoPersonResponse

router = APIRouter(prefix="/photos", tags=["Fotos"])

@router.post("/upload")
async def upload_photo(
    file: UploadFile = File(...),
    description: str | None = None,
    source: str | None = None,
    collection_id: int | None = None,
    user: Optional[User] = Depends(get_optional_current_user),
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
    
    # Associar ao contribuidor se estiver logado
    contributor_id = user.id if user else None
    
    photo = create_photo(
        db,
        file_name=file_name,
        file_path=file_path,
        file_hash=file_hash,
        description=description,
        source=source,
        collection_id=collection_id,
        contributor_id=contributor_id
    )
    return {
        "id": photo.id,
        "status": "upload_realizado",
        "photo_status": photo.status,
        "visibility": photo.visibility
    }


@router.get("/my")
def get_my_photos(
    skip: int = 0,
    limit: int = 50,
    status: str | None = None,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Lista as fotos enviadas pelo usuário logado.
    """
    from app.models.enums import PhotoStatus
    
    photo_status = None
    if status:
        try:
            photo_status = PhotoStatus(status)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Status inválido: {status}")
    
    photos = list_photos_by_contributor(
        db, 
        user.id, 
        skip=skip, 
        limit=limit, 
        status=photo_status
    )
    
    return [
        {
            "id": p.id,
            "file_name": p.file_name,
            "file_path": p.file_path,
            "description": p.description,
            "status": p.status.value,
            "visibility": p.visibility.value,
            "created_at": p.created_at.isoformat()
        }
        for p in photos
    ]


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
    curator: User = Depends(get_curator_user),
    db: Session = Depends(get_db)
):
    """
    Realiza curadoria de uma foto.
    Requer papel de curador ou administrador.
    """
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
        curator_name=curator.name,
        curator_id=curator.id
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
