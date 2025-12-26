from sqlalchemy.orm import Session
from app.models.photo import Photo
from app.models.enums import PhotoStatus, Visibility

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
