from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Role(Base):
    """
    Papéis de acesso no sistema.
    
    Papéis disponíveis:
    - user: Contribuidor - pode enviar fotos e acompanhar contribuições
    - curator: Curador - pode fazer curadoria, validar fotos, gerenciar histórias
    - admin: Administrador - acesso total ao sistema
    """
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(String(255))

    users = relationship("User", back_populates="role")
