# Sistema de Autenticação e Autorização

Este documento descreve o sistema de identidade, acesso e login implementado no projeto Retratos de Bonito.

## Visão Geral

O sistema permite:
- Registro de contribuidores
- Login com email e senha
- Controle de permissões por papel
- Proteção de rotas sensíveis
- Rastreamento de ações por usuário

## Papéis de Usuário

| Papel | Descrição | Permissões |
|-------|-----------|------------|
| `user` | Contribuidor | Enviar fotos, acompanhar contribuições |
| `curator` | Curador | Tudo de user + curadoria, validação, histórias |
| `admin` | Administrador | Acesso total, gerenciamento de usuários |

## Backend

### Endpoints de Autenticação

#### Registro
```http
POST /auth/register
Content-Type: application/json

{
  "name": "Maria Silva",
  "email": "maria@email.com",
  "password": "senhasegura123"
}
```

#### Login
```http
POST /auth/login
Content-Type: application/json

{
  "email": "maria@email.com",
  "password": "senhasegura123"
}
```

Retorna:
```json
{
  "access_token": "eyJ...",
  "token_type": "bearer",
  "expires_in": 86400
}
```

#### Perfil do Usuário
```http
GET /auth/me
Authorization: Bearer <token>
```

### Protegendo Rotas

#### Qualquer Usuário Logado
```python
from app.dependencies.auth import get_current_user

@router.get("/minha-rota")
def rota_protegida(user: User = Depends(get_current_user)):
    return {"usuario": user.name}
```

#### Papel Específico
```python
from app.dependencies.auth import require_role, get_curator_user

# Forma 1: Dependência pronta
@router.patch("/curadoria/{id}")
def curar_foto(user: User = Depends(get_curator_user)):
    ...

# Forma 2: Papéis dinâmicos
@router.delete("/admin/usuario/{id}")
def deletar_usuario(user: User = Depends(require_role("admin"))):
    ...
```

#### Usuário Opcional (Rotas Mistas)
```python
from app.dependencies.auth import get_optional_current_user

@router.post("/upload")
def upload(user: Optional[User] = Depends(get_optional_current_user)):
    if user:
        # Associar foto ao contribuidor
        contributor_id = user.id
    else:
        contributor_id = None
```

### Modelos de Dados

#### User
```python
class User(Base):
    id: int
    name: str
    email: str (único)
    password_hash: str
    role_id: int (FK -> roles)
    is_active: bool
    created_at: datetime
    updated_at: datetime
```

#### Role
```python
class Role(Base):
    id: int
    name: str (único: user, curator, admin)
    description: str
```

## Frontend

### Contexto de Autenticação

O `AuthProvider` em `lib/auth.tsx` gerencia toda a sessão:

```tsx
// Em qualquer componente
import { useAuth } from '@/lib/auth'

function MeuComponente() {
  const { 
    user,           // Dados do usuário ou null
    isAuthenticated, // Boolean
    isLoading,      // Carregando sessão
    login,          // Função de login
    register,       // Função de registro
    logout          // Função de logout
  } = useAuth()
}
```

### Requisições Autenticadas

```tsx
import { useAuthenticatedFetch } from '@/lib/auth'

function MeuComponente() {
  const authFetch = useAuthenticatedFetch()
  
  const carregarDados = async () => {
    const res = await authFetch('/photos/my')
    const data = await res.json()
  }
}
```

### Proteção de Páginas

```tsx
'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/lib/auth'

export default function PaginaProtegida() {
  const { isAuthenticated, isLoading } = useAuth()
  const router = useRouter()

  useEffect(() => {
    if (!isLoading && !isAuthenticated) {
      router.push('/login')
    }
  }, [isLoading, isAuthenticated, router])

  if (isLoading || !isAuthenticated) return null

  return <div>Conteúdo protegido</div>
}
```

### Páginas Disponíveis

| Rota | Descrição | Acesso |
|------|-----------|--------|
| `/login` | Tela de login | Público |
| `/register` | Tela de registro | Público |
| `/dashboard` | Painel do usuário | Autenticado |
| `/dashboard/minhas-fotos` | Fotos do contribuidor | Autenticado |
| `/curadoria` | Painel de curadoria | Curador/Admin |

## Migração

Para aplicar as alterações no banco de dados:

```bash
cd src
alembic upgrade head
```

## Configuração

### Variáveis de Ambiente

```bash
# Chave secreta para JWT (OBRIGATÓRIO em produção)
export SECRET_KEY="sua-chave-super-secreta-aqui"

# Tempo de expiração do token (opcional, padrão: 1440 minutos = 24h)
export ACCESS_TOKEN_EXPIRE_MINUTES="1440"
```

### Dependências

Novas dependências adicionadas ao `requirements.txt`:
- `passlib[bcrypt]>=1.7.4` - Hash de senhas
- `pyjwt>=2.8.0` - Tokens JWT
- `pydantic[email]>=2.0.0` - Validação de email

Instalar:
```bash
pip install -r requirements.txt
```

## Segurança

### Senhas
- Hash com bcrypt (passlib)
- Mínimo 6 caracteres
- Nunca armazenadas em texto puro

### Tokens
- JWT assinado com HS256
- Expiração configurável (padrão 24h)
- Inclui apenas user_id no payload

### Recomendações para Produção
1. Use uma `SECRET_KEY` forte e única
2. Configure HTTPS
3. Reduza tempo de expiração se necessário
4. Implemente rate limiting
5. Adicione logs de auditoria

## Estrutura de Arquivos

```
src/app/
├── config/
│   ├── __init__.py
│   └── security.py          # Configurações de segurança
├── dependencies/
│   ├── auth.py              # Dependências de autenticação
│   └── db.py
├── models/
│   ├── role.py              # Modelo Role
│   └── user.py              # Modelo User
├── repositories/
│   └── user_repository.py   # Operações de banco
├── routers/
│   └── auth.py              # Endpoints de autenticação
├── schemas/
│   └── auth.py              # Schemas Pydantic
└── services/
    └── auth_service.py      # Lógica de autenticação

src/frontend/
├── lib/
│   └── auth.tsx             # Contexto de autenticação
├── components/
│   ├── UserMenu.tsx         # Menu de usuário
│   └── ProtectedRoute.tsx   # Proteção de rotas
└── app/
    ├── login/page.tsx
    ├── register/page.tsx
    ├── dashboard/
    │   ├── page.tsx
    │   └── minhas-fotos/page.tsx
    └── curadoria/page.tsx
```

## Próximos Passos

Funcionalidades sugeridas para futuras versões:

1. **Recuperação de senha** - Email para reset
2. **Verificação de email** - Confirmação no registro
3. **OAuth** - Login com Google/Facebook
4. **Refresh tokens** - Renovação automática
5. **2FA** - Autenticação em dois fatores
6. **Logs de acesso** - Histórico de logins
