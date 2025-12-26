from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.database import Base

class Collection(Base):
    __tablename__ = "collections"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    origin: Mapped[str | None] = mapped_column(String(255))

    status: Mapped[str] = mapped_column(String(50), default="ativa")

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    created_by: Mapped[str | None] = mapped_column(String(255))

    photos = relationship("Photo", back_populates="collection")
