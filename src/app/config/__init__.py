"""
Módulo de configuração da aplicação.
"""

from app.config.security import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ACCESS_TOKEN_EXPIRE,
    ROLE_USER,
    ROLE_CURATOR,
    ROLE_ADMIN,
    VALID_ROLES,
)

__all__ = [
    "SECRET_KEY",
    "ALGORITHM",
    "ACCESS_TOKEN_EXPIRE_MINUTES",
    "ACCESS_TOKEN_EXPIRE",
    "ROLE_USER",
    "ROLE_CURATOR",
    "ROLE_ADMIN",
    "VALID_ROLES",
]
