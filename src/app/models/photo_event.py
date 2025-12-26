from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class PhotoEvent(Base):
    __tablename__ = "photo_events"

    photo_id: Mapped[int] = mapped_column(ForeignKey("photos.id"), primary_key=True)
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"), primary_key=True)

    photo = relationship("Photo", back_populates="events")
    event = relationship("Event", back_populates="photos")
