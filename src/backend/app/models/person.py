from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Person(Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    nickname: Mapped[str | None] = mapped_column(String(255))
    birth_year: Mapped[int | None]
    death_year: Mapped[int | None]
    notes: Mapped[str | None] = mapped_column(Text)

    photos = relationship("PhotoPerson", back_populates="person")
