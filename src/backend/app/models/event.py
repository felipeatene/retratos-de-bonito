from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    start_date: Mapped[str | None] = mapped_column(Date)
    end_date: Mapped[str | None] = mapped_column(Date)

    photos = relationship("PhotoEvent", back_populates="event")
