from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


# ============================================
# Schemas de Registro e Login
# ============================================

class UserRegisterRequest(BaseModel):
    """Dados para criar uma nova conta de contribuidor."""
    name: str = Field(..., min_length=2, max_length=255, description="Nome completo")
    email: EmailStr = Field(..., description="Email para acesso")
    password: str = Field(..., min_length=6, max_length=128, description="Senha de acesso")


class UserLoginRequest(BaseModel):
    """Credenciais para entrar na conta."""
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """Token de acesso retornado após login."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int = Field(..., description="Tempo de expiração em segundos")


# ============================================
# Schemas de Usuário
# ============================================

class RoleResponse(BaseModel):
    """Informações sobre o papel do usuário."""
    id: int
    name: str
    description: str | None = None

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    """Informações públicas do usuário."""
    id: int
    name: str
    email: str
    role: RoleResponse | None = None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserProfileResponse(BaseModel):
    """Perfil completo do usuário logado."""
    id: int
    name: str
    email: str
    role_name: str
    is_active: bool
    created_at: datetime
    
    # Estatísticas de contribuição
    total_photos: int = 0
    photos_validated: int = 0
    photos_pending: int = 0

    class Config:
        from_attributes = True


class UserUpdateRequest(BaseModel):
    """Dados para atualizar perfil."""
    name: str | None = Field(None, min_length=2, max_length=255)


class PasswordChangeRequest(BaseModel):
    """Dados para alterar senha."""
    current_password: str
    new_password: str = Field(..., min_length=6, max_length=128)


# ============================================
# Schemas de Gerenciamento (Admin)
# ============================================

class UserRoleUpdateRequest(BaseModel):
    """Alterar papel de um usuário (apenas admin)."""
    role_name: str = Field(..., description="Nome do papel: user, curator, admin")


class UserStatusUpdateRequest(BaseModel):
    """Ativar/desativar usuário (apenas admin)."""
    is_active: bool
