"""
Dependências de autenticação e autorização.

Fornece funções reutilizáveis para:
- Obter usuário atual
- Verificar papéis de acesso
- Proteger rotas por permissão
"""

from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.models.user import User
from app.services.auth_service import get_current_user_from_token
from app.config.security import ROLE_CURATOR, ROLE_ADMIN


# Esquema de autenticação Bearer
security = HTTPBearer(auto_error=False)


async def get_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependência que obtém o usuário atual a partir do token JWT.
    
    Uso:
        @router.get("/rota-protegida")
        def rota(user: User = Depends(get_current_user)):
            ...
    
    Raises:
        HTTPException 401: Se não autenticado ou token inválido
    """
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Autenticação necessária",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user = get_current_user_from_token(db, credentials.credentials)
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user


async def get_optional_current_user(
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(security),
    db: Session = Depends(get_db)
) -> Optional[User]:
    """
    Dependência que obtém o usuário atual, mas não exige autenticação.
    Útil para rotas que funcionam diferente para usuários logados.
    
    Uso:
        @router.get("/rota-publica")
        def rota(user: Optional[User] = Depends(get_optional_current_user)):
            if user:
                # Lógica para usuário logado
            else:
                # Lógica para visitante
    
    Returns:
        Usuário ou None se não autenticado
    """
    if credentials is None:
        return None
    
    return get_current_user_from_token(db, credentials.credentials)


def require_role(*allowed_roles: str):
    """
    Cria uma dependência que verifica se o usuário tem um dos papéis permitidos.
    
    Uso:
        @router.patch("/curadoria/{id}")
        def curar(
            id: int,
            user: User = Depends(require_role("curator", "admin"))
        ):
            ...
    
    Args:
        allowed_roles: Papéis que têm permissão de acesso
    
    Returns:
        Função de dependência que valida o papel
    
    Raises:
        HTTPException 403: Se usuário não tem papel permitido
    """
    async def role_checker(
        user: User = Depends(get_current_user)
    ) -> User:
        user_role = user.role_name
        
        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acesso restrito. Papel necessário: {', '.join(allowed_roles)}"
            )
        
        return user
    
    return role_checker


# Dependências prontas para papéis específicos
require_curator = require_role(ROLE_CURATOR, ROLE_ADMIN)
require_admin = require_role(ROLE_ADMIN)


async def get_curator_user(
    user: User = Depends(require_curator)
) -> User:
    """
    Dependência que exige papel de curador ou administrador.
    
    Uso:
        @router.patch("/curadoria/{id}")
        def curar(user: User = Depends(get_curator_user)):
            ...
    """
    return user


async def get_admin_user(
    user: User = Depends(require_admin)
) -> User:
    """
    Dependência que exige papel de administrador.
    
    Uso:
        @router.delete("/usuarios/{id}")
        def deletar(user: User = Depends(get_admin_user)):
            ...
    """
    return user
