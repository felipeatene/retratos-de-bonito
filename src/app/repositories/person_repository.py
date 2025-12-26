from sqlalchemy.orm import Session
from app.models.person import Person


def get_by_name(db: Session, full_name: str):
    return (
        db.query(Person)
        .filter(Person.full_name.ilike(full_name))
        .first()
    )


def create_person(
    db: Session,
    *,
    full_name: str,
    nickname: str | None = None,
    birth_year: int | None = None,
    death_year: int | None = None
):
    person = Person(
        full_name=full_name,
        nickname=nickname,
        birth_year=birth_year,
        death_year=death_year
    )
    db.add(person)
    db.commit()
    db.refresh(person)
    return person
