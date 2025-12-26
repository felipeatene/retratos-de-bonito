# 🔧 Backend — Guia Completo

**Retratos de Bonito API**

API FastAPI que gerencia fotos, pessoas, histórias e metadados do acervo.

---

## 🚀 Quick Start

### Requisitos
- Python 3.10+
- pip ou poetry

### Instalação

```bash
# Entrar na pasta do projeto
cd p:\Projetos\retratos-de-bonito

# Instalar dependências
pip install -r requirements.txt

# Criar/migrar banco de dados
alembic upgrade head

# Rodar o servidor
python -m uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000
```

**A API estará em:** http://localhost:8000

### Documentação Automática
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## 📁 Estrutura

```
src/app/
├── main.py                    # Entrada da aplicação
├── database.py                # Conexão SQLAlchemy
├── models/                    # ORM (SQLAlchemy)
│   ├── photo.py
│   ├── person.py
│   ├── story.py
│   ├── consent.py
│   └── ...
├── schemas/                   # Pydantic (validação)
│   ├── photo_curation.py
│   ├── public_photo.py
│   └── ...
├── repositories/              # Acesso a dados
│   ├── photo_repository.py
│   ├── person_repository.py
│   └── ...
├── routers/                   # Endpoints
│   ├── photos.py              # CRUD fotos
│   ├── people.py              # CRUD pessoas
│   ├── stories.py             # CRUD histórias
│   ├── public.py              # Endpoints públicos
│   └── consents.py            # Gerenciar consentimentos
└── services/                  # Lógica de negócio
    ├── photo_storage.py       # Upload/storage
    └── person_link_service.py # Reconhecimento facial
```

---

## 🔌 Endpoints Principais

### Públicos (Sem Auth)

#### Timeline (Modo Exposição)
```
GET /public/timeline
```
Retorna fotos agrupadas por década.

**Exemplo:**
```json
[
  {
    "decade": 1990,
    "photos": [
      {
        "photo_id": 1,
        "file_name": "2025/photo-001.jpg",
        "description": "Praça central",
        "original_date": "1995"
      }
    ]
  }
]
```

#### Busca Pública
```
GET /public/search?description=praça&location=centro
```

#### Detalhe da Foto
```
GET /public/photos/{photo_id}
```

#### Histórias de uma Foto
```
GET /public/photos/{photo_id}/stories
```

### Privados (Protegidos)

#### Upload de Foto
```
POST /photos/upload
Content-Type: multipart/form-data

file: File
description: string
source: string (opcional)
```

#### Curadoria de Foto
```
PUT /photos/{photo_id}/curate
{
  "status": "validated",
  "visibility": "public"
}
```

---

## 🗄️ Banco de Dados

### SQLite

Banco padrão: `retratos.db`

#### Tabelas Principais
- **photos** — Fotos do acervo
- **people** — Pessoas retratadas
- **stories** — Histórias/depoimentos
- **consents** — Consentimentos
- **photo_people** — Relacionamento foto-pessoa

### Migrações (Alembic)

```bash
# Ver migrações pendentes
alembic current

# Aplicar todas
alembic upgrade head

# Criar nova migração
alembic revision --autogenerate -m "descrição"

# Voltar versão anterior
alembic downgrade -1
```

---

## 🔐 Segurança

### Consentimento
- Toda foto enviada começa com `status = "bruta"`
- Só aparece em `/public` se `visibility = "public"`
- Curador revisa e aprova

### Hash de Arquivo
```python
import hashlib

def hash_file(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
```

### Visibilidade
```
photo.visibility = "private"   # Só curador vê
photo.visibility = "public"    # Acesso público
photo.visibility = "restricted" # Apenas com consent
```

---

## 📤 Upload de Fotos

### Fluxo

```
POST /photos/upload
├─ Validação: tipo, tamanho
├─ Storage: pasta dated (2025/01/...)
├─ Hash: duplicata check
├─ BD: photo.status = "bruta"
└─ Response: photo_id
```

### Tamanho Máximo
- Recomendado: 10MB
- Ajustável em `main.py`

### Formatos
- JPG, PNG, WebP
- Sem BMP, TIFF, GIF

---

## 🧪 Testes

```bash
# Rodar todos os testes
pytest

# Cobertura
pytest --cov=src.app

# Teste específico
pytest scripts/test_add_person.py -v
```

### Scripts de Teste

```bash
# Verificar estrutura do BD
python scripts/check_tables.py

# Listar tabelas
python scripts/list_tables.py

# Teste de curadores
python scripts/run_curate_test.py

# Teste de consentimentos
python scripts/test_consents.py
```

---

## 🚀 Deployment

### Docker (Futuro)

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Variáveis de Ambiente

```env
DATABASE_URL=sqlite:///retratos.db
API_TITLE=Retratos de Bonito
API_VERSION=1.0.0
STORAGE_PATH=./storage/photos
MAX_FILE_SIZE=10485760  # 10MB em bytes
```

---

## 📚 Referência de Rotas

### Photos (`routers/photos.py`)
- `GET /photos/` — Listar todas
- `POST /photos/` — Criar nova
- `GET /photos/{id}` — Detalhe
- `PUT /photos/{id}` — Atualizar
- `DELETE /photos/{id}` — Deletar
- `POST /photos/upload` — Upload com form-data

### People (`routers/people.py`)
- `GET /people/` — Listar
- `POST /people/` — Adicionar
- `GET /people/{id}` — Detalhe
- `PUT /people/{id}` — Atualizar

### Stories (`routers/stories.py`)
- `GET /stories/` — Listar
- `POST /stories/` — Criar
- `GET /stories/{id}` — Detalhe
- `DELETE /stories/{id}` — Deletar

### Public (`routers/public.py`)
- `GET /public/timeline` — Exposição
- `GET /public/search` — Busca
- `GET /public/photos/{id}` — Detalhe
- `GET /public/photos/{id}/stories` — Histórias

---

## 🔧 Troubleshooting

### "Módulo não encontrado"
```bash
pip install -r requirements.txt
# ou
pip install -e .
```

### "Banco de dados corrompido"
```bash
rm retratos.db
alembic upgrade head
```

### "Erro ao fazer upload"
- Verificar `/storage/photos` existe
- Verificar permissões de escrita
- Verificar `MAX_FILE_SIZE` em `.env`

---

## 📞 Debug

```python
# Ver todas as rotas
from src.app.main import app

for route in app.routes:
    print(f"{route.methods} {route.path}")
```

---

## 📖 Documentação Adicional

- [LGPD Compliance](../docs/privacy.md)
- [Estrutura de Dados](../DOCS.md)
- [Ética e Consentimento](../docs/metodologia.md)

---

<div align="center">

**Backend do Retratos de Bonito — Preservando dados com segurança e ética** 🔒✨

</div>
