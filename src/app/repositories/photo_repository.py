from sqlalchemy.orm import Session
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
    collection_id: int | None = None
):
    photo = Photo(
        file_name=file_name,
        file_path=file_path,
        file_hash=file_hash,
        description=description,
        source=source,
        collection_id=collection_id,
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
    curator_name: str | None = None
):
    if status:
        photo.status = status
    if visibility:
        photo.visibility = visibility

    db.commit()
    db.refresh(photo)

    # registrar curadoria para futura auditoria (não apaga nada)
    if curator_name:
        log = AuditLog(
            user_id=None,
            entity="photo",
            entity_id=photo.id,
            action="curate",
            details=f"curator={curator_name} status={status} visibility={visibility}"
        )
        db.add(log)
        db.commit()

    return photo
