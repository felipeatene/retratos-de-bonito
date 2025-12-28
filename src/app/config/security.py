"""
Configurações de segurança e autenticação.

Este módulo centraliza as configurações sensíveis do sistema.
Em produção, use variáveis de ambiente para SECRET_KEY.
"""

import os
from datetime import timedelta

# Chave secreta para assinatura de tokens JWT
# Em produção, defina via variável de ambiente: export SECRET_KEY="sua-chave-secreta-aqui"
SECRET_KEY = os.getenv("SECRET_KEY", "retratos-bonito-dev-secret-key-change-in-production")

# Algoritmo de criptografia do JWT
ALGORITHM = "HS256"

# Tempo de expiração do token de acesso
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))  # 24 horas

# Tempo de expiração como timedelta
ACCESS_TOKEN_EXPIRE = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

# Configurações de senha
PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 128

# Papéis disponíveis no sistema
ROLE_USER = "user"
ROLE_CURATOR = "curator"
ROLE_ADMIN = "admin"

# Lista de papéis válidos
VALID_ROLES = [ROLE_USER, ROLE_CURATOR, ROLE_ADMIN]
