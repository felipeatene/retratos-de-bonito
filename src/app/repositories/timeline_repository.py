from sqlalchemy.orm import Session
from app.models.photo import Photo
from app.models.enums import PhotoStatus, Visibility


def timeline_by_decade(db: Session):
    photos = (
        db.query(Photo)
        .filter(
            Photo.status == PhotoStatus.VALIDADA,
            Photo.visibility == Visibility.PUBLICA,
            Photo.original_date.isnot(None)
        )
        .order_by(Photo.original_date.asc())
        .all()
    )

    timeline: dict[int, list[Photo]] = {}

    for photo in photos:
        try:
            year = int(photo.original_date[:4])
            decade = (year // 10) * 10
        except (ValueError, TypeError):
            continue

        timeline.setdefault(decade, []).append(photo)

    return timeline
