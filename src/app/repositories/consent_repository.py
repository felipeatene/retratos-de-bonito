from sqlalchemy.orm import Session
from app.models.consent import Consent
from datetime import date


def _parse_date(val):
    if not val:
        return None
    if isinstance(val, date):
        return val
    try:
        return date.fromisoformat(val)
    except Exception:
        return None


def get_consent(
    db: Session,
    *,
    photo_id: int,
    person_id: int
):
    return (
        db.query(Consent)
        .filter(
            Consent.photo_id == photo_id,
            Consent.person_id == person_id
        )
        .first()
    )


def create_or_update_consent(
    db: Session,
    *,
    photo_id: int,
    person_id: int,
    consent_type,
    consent_date=None,
    notes=None
):
    consent = get_consent(
        db,
        photo_id=photo_id,
        person_id=person_id
    )

    if consent:
        consent.consent_type = consent_type
        consent.consent_date = _parse_date(consent_date)
        consent.notes = notes
    else:
        consent = Consent(
            photo_id=photo_id,
            person_id=person_id,
            consent_type=consent_type,
            consent_date=_parse_date(consent_date),
            notes=notes
        )
        db.add(consent)

    db.commit()
    db.refresh(consent)
    return consent
