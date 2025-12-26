from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class PhotoPerson(Base):
    __tablename__ = "photo_people"

    photo_id: Mapped[int] = mapped_column(ForeignKey("photos.id"), primary_key=True)
    person_id: Mapped[int] = mapped_column(ForeignKey("people.id"), primary_key=True)
    role: Mapped[str] = mapped_column(String(100), default="retratado")

    photo = relationship("Photo", back_populates="people")
    person = relationship("Person", back_populates="photos")
