from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.services.photo_storage import calculate_hash, save_photo_file
from app.repositories.photo_repository import get_by_hash, create_photo

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
