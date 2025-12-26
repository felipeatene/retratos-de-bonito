# 🏛️ Retratos de Bonito — Documentação Completa

Preservação da memória visual de Bonito (MS) com acesso seguro, consentido e ético.

## 📊 API — Endpoints Principais

### Públicos (sem autenticação)

#### Timeline
```
GET /public/timeline
```
Retorna fotos agrupadas por década (status VALIDADA + PUBLICA).

#### Busca
```
GET /public/search?text=...&person=...&year=...&location=...
```
Filtra fotos públicas por texto, pessoa, ano, local.

#### Detalhe da Foto
```
GET /public/photos/{id}
```
Foto completa com pessoas (filtradas por consentimento) e histórias públicas.

#### Histórias Públicas
```
GET /public/photos/{id}/stories
```
Histórias com `visibility=PUBLICA` de uma foto.

---

### Internos (admin/curador)

#### Upload de Foto
```
POST /photos
```
Cria nova foto. Requer arquivo + metadados.

#### Vincular Pessoa
```
POST /photos/{id}/people
```
Liga pessoa (existente ou cria) a uma foto.

#### Atualizar Curadoria
```
PATCH /photos/{id}/curate
```
Muda status (PENDENTE/VALIDADA) e visibilidade (PRIVADA/RESTRITA/PUBLICA).

#### Fotos de Uma Pessoa
```
GET /people/{id}/photos
```
Lista todas as fotos em que uma pessoa aparece.

#### Criar História
```
POST /stories/photos/{id}
```
Vincula história/depoimento a uma foto.

#### Consentimento
```
POST /consents/photos/{id}/people/{person_id}
GET /consents/photos/{id}/people/{person_id}
```
Registra ou consulta consentimento de pessoa para exposição pública.

---

## 🔐 Regras de Privacidade & Consentimento

### Fotos
- **Pública:** Aparece em busca + timeline se `status=VALIDADA` **E** `visibility=PUBLICA`
- **Restrita:** Visível apenas para usuários logados/especificados
- **Privada:** Nunca pública (mas pode ser consultada internamente)

### Pessoas
- **Sem Consentimento:** Aparecem em detalhe público (padrão)
- **Consentimento Público:** Aparecem explicitamente
- **Sem Consentimento Registrado:** Aparecem com informações básicas

### Histórias
- **PUBLICA:** Mostrada em `/public/photos/{id}/stories`
- **RESTRITA/PRIVADA:** Ocultas em buscas públicas

---

## 🗄️ Banco de Dados

SQLite (`retratos.db`) com tabelas:

| Tabela | Descrição |
|--------|-----------|
| `photos` | Fotografias (id, file_name, description, status, visibility, original_date, source) |
| `people` | Pessoas (id, full_name, nickname, birth_year, death_year, role) |
| `photo_people` | Vínculo M:N entre fotos e pessoas |
| `stories` | Histórias/depoimentos (title, content, author_name, author_relation, visibility) |
| `consents` | Consentimento de pessoa para exposição pública (consent_type, consent_date) |
| `locations` | Locais mencionados (name, description) |
| `events` | Eventos contextuais (name, date, description) |
| `photo_events` | Vínculo entre fotos e eventos |
| `collections` | Coleções temáticas (name, description) |
| `audit_logs` | Rastreamento de mudanças (table_name, record_id, action, changed_by, changed_at) |
| `alembic_version` | Controle de migrações |

---

## 🌐 Frontend (Estático)

Localizado em `src/frontend_static/`. Sem dependências Node — apenas HTML + JS vanilla + Tailwind CDN.

### Páginas

| Página | URL | Descrição |
|--------|-----|-----------|
| Timeline | `/` | Fotos por década |
| Busca | `/search.html` | Filtro avançado |
| Detalhe | `/photo.html?id=1` | Foto + pessoas + histórias |

### Features
- Responsivo (mobile, tablet, desktop)
- Download com termo de uso
- Navegação fluida
- Zero build step

---

## 🎯 Ética & Design

### Princípios
- ✅ **Consentimento explícito** — Pessoas apenas expostas se aprovarem
- ✅ **Sem edição silenciosa** — Todas as mudanças em `audit_logs`
- ✅ **Memória comunitária** — Histórias orais registradas permanentemente
- ✅ **Acesso igualitário** — Frontend público sem login

### Segurança
- Fotos privadas nunca retornam em buscas públicas
- Consentimento de data — rastreia quando foi dado
- Auditoria completa de mudanças
- Senhas hasheadas (quando houver auth)

---

## 💾 Dependências & Stack

- **Backend:** Python 3.14, FastAPI, SQLAlchemy, Pydantic, Alembic
- **Frontend:** HTML5, JavaScript ES6, Tailwind CSS (CDN)
- **Banco:** SQLite
- **Servidor:** Uvicorn (dev), HTTP server (frontend)

Instalar:
```bash
pip install -r requirements.txt
```

---

## 🛠️ Desenvolvimento

### Adicionar uma tabela
```bash
export PYTHONPATH=src
python
from app.models.nova import Nova
from app.database import engine, Base
Base.metadata.create_all(engine)  # ou usar Alembic
```

### Rodar migration
```bash
alembic revision --autogenerate -m "desc"
alembic upgrade head
```

### Testar endpoint
```bash
curl http://127.0.0.1:8000/public/timeline | jq
```

---

## 📝 Exemplo de Fluxo

1. **Curador upload foto**
   - POST `/photos` + imagem
   - Status: PENDENTE, Visibility: PRIVADA

2. **Curador vincula pessoas**
   - POST `/photos/{id}/people` + nome/info
   - Cria Person se não existir

3. **Pessoa registra consentimento**
   - POST `/consents/photos/{id}/people/{person_id}`
   - Consent Type: PUBLICO
   - Consent Date: hoje

4. **Curador valida & publica**
   - PATCH `/photos/{id}/curate` → Status: VALIDADA, Visibility: PUBLICA

5. **Público explora**
   - GET `/public/timeline` → vê foto agrupada por década
   - GET `/public/photos/{id}` → vê detalhe + pessoa com consentimento
   - GET `/public/photos/{id}/stories` → vê histórias públicas

---

## 🚀 Deploy

Frontend: Deploy estático em Vercel/Netlify (copiar `src/frontend_static/` ou usar `src/frontend/` com Next.js build).

Backend: Deploy em Render/Railway com variáveis:
- `DATABASE_URL=sqlite:///retratos.db`
- Ou PostgreSQL em produção

---

**Retratos de Bonito** — Preservando memória, celebrando pertencimento. 📸
