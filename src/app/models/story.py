from sqlalchemy import String, Text, ForeignKey, DateTime, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.database import Base
from app.models.enums import Visibility


class Story(Base):
    __tablename__ = "stories"

    id: Mapped[int] = mapped_column(primary_key=True)
    photo_id: Mapped[int] = mapped_column(ForeignKey("photos.id"))

    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text)

    author_name: Mapped[str | None] = mapped_column(String(255))
    author_relation: Mapped[str | None] = mapped_column(String(255))

    visibility: Mapped[Visibility] = mapped_column(
        Enum(Visibility),
        default=Visibility.RESTRITA
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    photo = relationship("Photo")
