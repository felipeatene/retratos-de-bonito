from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
from app.models.photo import Photo
from app.models.enums import PhotoStatus, Visibility
from app.models.audit_log import AuditLog

def get_by_hash(db: Session, file_hash: str):
    return db.query(Photo).filter(Photo.file_hash == file_hash).first()

def create_photo(
    db: Session,
    *,
    file_name: str,
    file_path: str,
    file_hash: str,
    description: str | None = None,
    source: str | None = None,
    collection_id: int | None = None,
    contributor_id: int | None = None
):
    photo = Photo(
        file_name=file_name,
        file_path=file_path,
        file_hash=file_hash,
        description=description,
        source=source,
        collection_id=collection_id,
        contributor_id=contributor_id,
        status=PhotoStatus.BRUTA,
        visibility=Visibility.RESTRITA,
    )
    db.add(photo)
    db.commit()
    db.refresh(photo)
    return photo


def update_photo_curation(
    db: Session,
    *,
    photo: Photo,
    status=None,
    visibility=None,
    curator_name: str | None = None,
    curator_id: int | None = None
):
    if status:
        photo.status = status
    if visibility:
        photo.visibility = visibility

    db.commit()
    db.refresh(photo)

    # registrar curadoria para futura auditoria (não apaga nada)
    log = AuditLog(
        user_id=curator_id,
        entity="photo",
        entity_id=photo.id,
        action="curate",
        details=f"curator={curator_name or curator_id} status={status} visibility={visibility}"
    )
    db.add(log)
    db.commit()

    return photo


def count_photos_by_contributor(
    db: Session,
    contributor_id: int,
    status: Optional[PhotoStatus] = None
) -> int:
    """
    Conta fotos enviadas por um contribuidor.
    
    Args:
        db: Sessão do banco de dados
        contributor_id: ID do contribuidor
        status: Filtrar por status específico (opcional)
    
    Returns:
        Número de fotos
    """
    query = db.query(func.count(Photo.id)).filter(
        Photo.contributor_id == contributor_id
    )
    
    if status:
        query = query.filter(Photo.status == status)
    
    return query.scalar() or 0


def list_photos_by_contributor(
    db: Session,
    contributor_id: int,
    *,
    skip: int = 0,
    limit: int = 50,
    status: Optional[PhotoStatus] = None
):
    """
    Lista fotos enviadas por um contribuidor.
    """
    query = db.query(Photo).filter(Photo.contributor_id == contributor_id)
    
    if status:
        query = query.filter(Photo.status == status)
    
    return query.order_by(Photo.created_at.desc()).offset(skip).limit(limit).all()
