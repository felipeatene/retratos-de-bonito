from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional, List

from app.models.user import User
from app.models.role import Role


# ============================================
# Funções de Role (Papéis)
# ============================================

def get_role_by_name(db: Session, name: str) -> Optional[Role]:
    """Busca papel pelo nome."""
    return db.query(Role).filter(Role.name == name).first()


def get_role_by_id(db: Session, role_id: int) -> Optional[Role]:
    """Busca papel pelo ID."""
    return db.query(Role).filter(Role.id == role_id).first()


def get_all_roles(db: Session) -> List[Role]:
    """Lista todos os papéis disponíveis."""
    return db.query(Role).all()


def create_role(
    db: Session,
    *,
    name: str,
    description: str | None = None
) -> Role:
    """Cria um novo papel."""
    role = Role(name=name, description=description)
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


def ensure_default_roles(db: Session) -> None:
    """
    Garante que os papéis padrão existam no banco.
    Chamado durante a inicialização da aplicação.
    """
    default_roles = [
        ("user", "Contribuidor - pode enviar fotos e acompanhar contribuições"),
        ("curator", "Curador - pode fazer curadoria, validar fotos e gerenciar histórias"),
        ("admin", "Administrador - acesso total ao sistema"),
    ]
    
    for name, description in default_roles:
        existing = get_role_by_name(db, name)
        if not existing:
            create_role(db, name=name, description=description)


# ============================================
# Funções de User (Usuários)
# ============================================

def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    """Busca usuário pelo ID."""
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """Busca usuário pelo email."""
    return db.query(User).filter(User.email == email).first()


def get_active_user_by_email(db: Session, email: str) -> Optional[User]:
    """Busca usuário ativo pelo email."""
    return (
        db.query(User)
        .filter(User.email == email, User.is_active == True)
        .first()
    )


def create_user(
    db: Session,
    *,
    name: str,
    email: str,
    password_hash: str,
    role_id: int | None = None
) -> User:
    """
    Cria um novo usuário/contribuidor.
    Se role_id não for informado, busca o papel 'user' padrão.
    """
    if role_id is None:
        default_role = get_role_by_name(db, "user")
        if default_role:
            role_id = default_role.id
    
    user = User(
        name=name,
        email=email,
        password_hash=password_hash,
        role_id=role_id
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(
    db: Session,
    user: User,
    *,
    name: str | None = None,
    password_hash: str | None = None
) -> User:
    """Atualiza dados do usuário."""
    if name is not None:
        user.name = name
    if password_hash is not None:
        user.password_hash = password_hash
    
    db.commit()
    db.refresh(user)
    return user


def update_user_role(
    db: Session,
    user: User,
    role_id: int
) -> User:
    """Atualiza o papel do usuário (apenas admin)."""
    user.role_id = role_id
    db.commit()
    db.refresh(user)
    return user


def update_user_status(
    db: Session,
    user: User,
    is_active: bool
) -> User:
    """Ativa ou desativa um usuário (apenas admin)."""
    user.is_active = is_active
    db.commit()
    db.refresh(user)
    return user


def list_users(
    db: Session,
    *,
    skip: int = 0,
    limit: int = 50,
    role_name: str | None = None,
    is_active: bool | None = None
) -> List[User]:
    """Lista usuários com filtros opcionais."""
    query = db.query(User)
    
    if role_name:
        query = query.join(Role).filter(Role.name == role_name)
    
    if is_active is not None:
        query = query.filter(User.is_active == is_active)
    
    return query.offset(skip).limit(limit).all()


def count_users(
    db: Session,
    *,
    role_name: str | None = None,
    is_active: bool | None = None
) -> int:
    """Conta usuários com filtros opcionais."""
    query = db.query(func.count(User.id))
    
    if role_name:
        query = query.join(Role).filter(Role.name == role_name)
    
    if is_active is not None:
        query = query.filter(User.is_active == is_active)
    
    return query.scalar() or 0
