"""
Rotas de autenticação.

Endpoints para registro, login e gerenciamento de conta.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.dependencies.auth import get_current_user, get_admin_user
from app.models.user import User
from app.schemas.auth import (
    UserRegisterRequest,
    UserLoginRequest,
    TokenResponse,
    UserResponse,
    UserProfileResponse,
    UserUpdateRequest,
    PasswordChangeRequest,
    UserRoleUpdateRequest,
    UserStatusUpdateRequest,
)
from app.services.auth_service import (
    register_user,
    login_user,
    hash_password,
    verify_password,
)
from app.repositories.user_repository import (
    update_user,
    get_user_by_id,
    get_role_by_name,
    update_user_role,
    update_user_status,
    list_users,
    count_users,
)
from app.repositories.photo_repository import count_photos_by_contributor
from app.models.enums import PhotoStatus


router = APIRouter(prefix="/auth", tags=["Autenticação"])


# ============================================
# Endpoints Públicos
# ============================================

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar conta",
    description="Crie uma conta para contribuir com a memória da cidade."
)
def register(
    request: UserRegisterRequest,
    db: Session = Depends(get_db)
):
    """
    Registra um novo contribuidor na plataforma.
    
    Após criar a conta, você poderá:
    - Enviar fotografias históricas
    - Contar histórias sobre as fotos
    - Acompanhar suas contribuições
    """
    try:
        user = register_user(db, request)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post(
    "/login",
    response_model=TokenResponse,
    summary="Entrar",
    description="Faça login para acessar sua conta."
)
def login(
    request: UserLoginRequest,
    db: Session = Depends(get_db)
):
    """
    Autentica o usuário e retorna um token de acesso.
    
    Use o token retornado no header Authorization:
    `Authorization: Bearer <token>`
    """
    result = login_user(db, request)
    
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return result


# ============================================
# Endpoints Autenticados
# ============================================

@router.get(
    "/me",
    response_model=UserProfileResponse,
    summary="Meu perfil",
    description="Veja suas informações e estatísticas de contribuição."
)
def get_me(
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Retorna o perfil do usuário logado com estatísticas.
    """
    # Busca estatísticas de contribuição
    try:
        total_photos = count_photos_by_contributor(db, user.id)
        photos_validated = count_photos_by_contributor(
            db, user.id, status=PhotoStatus.VALIDADA
        )
        photos_pending = count_photos_by_contributor(
            db, user.id, status=PhotoStatus.BRUTA
        )
    except Exception:
        # Se função não existir ainda, retorna zeros
        total_photos = 0
        photos_validated = 0
        photos_pending = 0
    
    return UserProfileResponse(
        id=user.id,
        name=user.name,
        email=user.email,
        role_name=user.role_name,
        is_active=user.is_active,
        created_at=user.created_at,
        total_photos=total_photos,
        photos_validated=photos_validated,
        photos_pending=photos_pending,
    )


@router.patch(
    "/me",
    response_model=UserResponse,
    summary="Atualizar perfil",
    description="Atualize seu nome."
)
def update_me(
    request: UserUpdateRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Atualiza os dados do perfil do usuário logado.
    """
    updated_user = update_user(
        db,
        user,
        name=request.name
    )
    return updated_user


@router.post(
    "/me/change-password",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Alterar senha",
    description="Altere sua senha de acesso."
)
def change_password(
    request: PasswordChangeRequest,
    user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Altera a senha do usuário logado.
    Requer a senha atual para confirmação.
    """
    # Verifica senha atual
    if not verify_password(request.current_password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Senha atual incorreta"
        )
    
    # Atualiza para nova senha
    new_hash = hash_password(request.new_password)
    update_user(db, user, password_hash=new_hash)


# ============================================
# Endpoints de Administração
# ============================================

@router.get(
    "/users",
    response_model=list[UserResponse],
    summary="Listar usuários",
    description="Lista todos os usuários (apenas administradores)."
)
def get_users(
    skip: int = 0,
    limit: int = 50,
    role: str | None = None,
    active: bool | None = None,
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """
    Lista usuários com filtros opcionais.
    Apenas administradores podem acessar.
    """
    users = list_users(
        db,
        skip=skip,
        limit=limit,
        role_name=role,
        is_active=active
    )
    return users


@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
    summary="Detalhes do usuário",
    description="Veja detalhes de um usuário (apenas administradores)."
)
def get_user(
    user_id: int,
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """
    Retorna detalhes de um usuário específico.
    """
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    return user


@router.patch(
    "/users/{user_id}/role",
    response_model=UserResponse,
    summary="Alterar papel",
    description="Altera o papel de um usuário (apenas administradores)."
)
def update_role(
    user_id: int,
    request: UserRoleUpdateRequest,
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """
    Altera o papel de um usuário.
    Papéis válidos: user, curator, admin
    """
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    
    role = get_role_by_name(db, request.role_name)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Papel inválido: {request.role_name}"
        )
    
    updated_user = update_user_role(db, user, role.id)
    return updated_user


@router.patch(
    "/users/{user_id}/status",
    response_model=UserResponse,
    summary="Ativar/desativar usuário",
    description="Ativa ou desativa um usuário (apenas administradores)."
)
def update_status(
    user_id: int,
    request: UserStatusUpdateRequest,
    admin: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    """
    Ativa ou desativa um usuário.
    Usuários desativados não podem fazer login.
    """
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    
    # Não permite desativar a si mesmo
    if user.id == admin.id and not request.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Você não pode desativar sua própria conta"
        )
    
    updated_user = update_user_status(db, user, request.is_active)
    return updated_user
