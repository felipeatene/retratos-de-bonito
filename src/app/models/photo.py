from sqlalchemy import String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.database import Base
from app.models.enums import PhotoStatus, Visibility

class Photo(Base):
    __tablename__ = "photos"

    id: Mapped[int] = mapped_column(primary_key=True)

    collection_id: Mapped[int | None] = mapped_column(ForeignKey("collections.id"))
    location_id: Mapped[int | None] = mapped_column(ForeignKey("locations.id"))
    contributor_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))

    file_name: Mapped[str] = mapped_column(String(255), nullable=False)
    file_path: Mapped[str] = mapped_column(String(500), nullable=False)
    file_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)

    original_date: Mapped[str | None] = mapped_column(String(50))
    digitized_date: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    description: Mapped[str | None] = mapped_column(Text)
    source: Mapped[str | None] = mapped_column(String(255))

    status: Mapped[PhotoStatus] = mapped_column(Enum(PhotoStatus), default=PhotoStatus.BRUTA)
    visibility: Mapped[Visibility] = mapped_column(Enum(Visibility), default=Visibility.RESTRITA)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    collection = relationship("Collection", back_populates="photos")
    location = relationship("Location", back_populates="photos")
    contributor = relationship("User", backref="contributed_photos")
    people = relationship("PhotoPerson", back_populates="photo")
    events = relationship("PhotoEvent", back_populates="photo")
