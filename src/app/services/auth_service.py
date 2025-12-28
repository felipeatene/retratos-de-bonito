"""
Serviço de autenticação.

Responsável por:
- Hash de senhas
- Criação e validação de tokens JWT
- Registro e login de usuários
"""

from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config.security import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from app.models.user import User
from app.repositories.user_repository import (
    get_user_by_email,
    get_active_user_by_email,
    create_user,
    get_user_by_id,
)
from app.schemas.auth import (
    UserRegisterRequest,
    UserLoginRequest,
    TokenResponse,
)


# Contexto de criptografia para senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ============================================
# Funções de Hash de Senha
# ============================================

def hash_password(password: str) -> str:
    """Gera hash seguro da senha usando bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica se a senha corresponde ao hash."""
    return pwd_context.verify(plain_password, hashed_password)


# ============================================
# Funções de Token JWT
# ============================================

def create_access_token(
    data: dict,
    expires_delta: timedelta | None = None
) -> str:
    """
    Cria um token JWT com os dados fornecidos.
    
    Args:
        data: Dados a serem codificados no token (geralmente user_id)
        expires_delta: Tempo de expiração personalizado
    
    Returns:
        Token JWT como string
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """
    Decodifica e valida um token JWT.
    
    Args:
        token: Token JWT a ser validado
    
    Returns:
        Dados decodificados ou None se inválido/expirado
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def get_user_id_from_token(token: str) -> Optional[int]:
    """
    Extrai o ID do usuário de um token válido.
    
    Args:
        token: Token JWT
    
    Returns:
        ID do usuário ou None se token inválido
    """
    payload = decode_access_token(token)
    if payload is None:
        return None
    
    user_id = payload.get("sub")
    if user_id is None:
        return None
    
    try:
        return int(user_id)
    except (ValueError, TypeError):
        return None


# ============================================
# Serviços de Autenticação
# ============================================

def register_user(
    db: Session,
    request: UserRegisterRequest
) -> User:
    """
    Registra um novo contribuidor na plataforma.
    
    Args:
        db: Sessão do banco de dados
        request: Dados de registro
    
    Returns:
        Usuário criado
    
    Raises:
        ValueError: Se email já estiver em uso
    """
    # Verifica se email já existe
    existing = get_user_by_email(db, request.email)
    if existing:
        raise ValueError("Este email já está em uso")
    
    # Cria hash da senha
    password_hash = hash_password(request.password)
    
    # Cria usuário
    user = create_user(
        db,
        name=request.name,
        email=request.email,
        password_hash=password_hash
    )
    
    return user


def authenticate_user(
    db: Session,
    request: UserLoginRequest
) -> Optional[User]:
    """
    Autentica um usuário por email e senha.
    
    Args:
        db: Sessão do banco de dados
        request: Credenciais de login
    
    Returns:
        Usuário autenticado ou None se credenciais inválidas
    """
    user = get_active_user_by_email(db, request.email)
    
    if not user:
        return None
    
    if not verify_password(request.password, user.password_hash):
        return None
    
    return user


def login_user(
    db: Session,
    request: UserLoginRequest
) -> Optional[TokenResponse]:
    """
    Realiza login e retorna token de acesso.
    
    Args:
        db: Sessão do banco de dados
        request: Credenciais de login
    
    Returns:
        TokenResponse com access_token ou None se credenciais inválidas
    """
    user = authenticate_user(db, request)
    
    if not user:
        return None
    
    # Cria token com ID do usuário
    access_token = create_access_token(data={"sub": str(user.id)})
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60  # Em segundos
    )


def get_current_user_from_token(
    db: Session,
    token: str
) -> Optional[User]:
    """
    Obtém o usuário atual a partir do token.
    
    Args:
        db: Sessão do banco de dados
        token: Token JWT
    
    Returns:
        Usuário ou None se token inválido
    """
    user_id = get_user_id_from_token(token)
    
    if user_id is None:
        return None
    
    user = get_user_by_id(db, user_id)
    
    if user is None or not user.is_active:
        return None
    
    return user
