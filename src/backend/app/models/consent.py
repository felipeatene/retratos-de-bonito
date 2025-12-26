from sqlalchemy import ForeignKey, Date, Text, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import ConsentType

class Consent(Base):
    __tablename__ = "consents"

    id: Mapped[int] = mapped_column(primary_key=True)
    photo_id: Mapped[int] = mapped_column(ForeignKey("photos.id"))
    person_id: Mapped[int] = mapped_column(ForeignKey("people.id"))

    consent_type: Mapped[ConsentType] = mapped_column(Enum(ConsentType))
    consent_date: Mapped[str | None] = mapped_column(Date)
    notes: Mapped[str | None] = mapped_column(Text)
