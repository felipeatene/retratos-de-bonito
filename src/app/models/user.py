from sqlalchemy import String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.database import Base


class User(Base):
    """
    Contribuidores e membros da comunidade.
    
    Cada pessoa que cria uma conta pode contribuir com fotos,
    histórias e ajudar a preservar a memória de Bonito.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    
    role_id: Mapped[int | None] = mapped_column(ForeignKey("roles.id"))
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime | None] = mapped_column(DateTime, onupdate=datetime.utcnow)

    role = relationship("Role", back_populates="users")

    @property
    def role_name(self) -> str:
        """Retorna o nome do papel do usuário ou 'user' como padrão."""
        return self.role.name if self.role else "user"
