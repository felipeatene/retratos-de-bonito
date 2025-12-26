from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int | None]
    entity: Mapped[str] = mapped_column(String(100))
    entity_id: Mapped[int]
    action: Mapped[str] = mapped_column(String(50))
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    details: Mapped[str | None]
