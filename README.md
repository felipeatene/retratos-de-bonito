<div align="center">

# 🌿📸 Retratos de Bonito 💧

**Museu Digital Comunitário — Preservação Ética da Memória Visual de Bonito (MS)**

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Next.js 14](https://img.shields.io/badge/frontend-Next.js%2014-black)](https://nextjs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Plataforma de arquivo fotográfico comunitário que coloca **ética, consentimento e privacidade** no centro da arquitetura técnica.

[Início Rápido](#-início-rápido) • [Funcionalidades](#-funcionalidades-principais) • [Tecnologias](#-tecnologias) • [Documentação](src/docs/) • [Contribuir](#-como-contribuir)

</div>

---

## 📖 Sobre o Projeto

**Retratos de Bonito** é uma plataforma de arquivo fotográfico comunitário desenvolvida para preservar a memória visual de Bonito, Mato Grosso do Sul. Diferente de simples galerias online, este projeto implementa **privacy-by-design** (privacidade por design):

### Por Que Este Projeto Existe?

Fotografias antigas contêm histórias, rostos e memórias de gerações que merecem ser preservadas com **dignidade**. Este sistema foi projetado para:

- ✅ **Respeitar a privacidade** das pessoas fotografadas
- ✅ **Rastrear consentimento** para exposição pública (LGPD-compliant)
- ✅ **Auditar todas as mudanças** em registros sensíveis (accountability)
- ✅ **Dar voz à comunidade** através de depoimentos orais vinculados às fotos
- ✅ **Permitir acesso público** sem vigilância ou coleta de dados
- ✅ **Integrar-se a museus e escolas** via modo exposição imersivo

### Público-Alvo

- **Comunidade de Bonito-MS**: Contribuir e explorar memórias familiares
- **Museus e centros culturais**: Exibir acervo em modo kiosk
- **Pesquisadores**: Buscar registros históricos com filtros avançados
- **Escolas**: Projetos de história local
- **Desenvolvedores**: Referência de sistema ético de arquivo digital

---

## 🚀 Início Rápido

### ⚠️ Pré-requisitos

Antes de começar, instale:

1. **Python 3.10+** — [Download](https://www.python.org/downloads/)
2. **Node.js 18+** — [Download](https://nodejs.org/) (escolha versão LTS)
3. **Git** — [Download](https://git-scm.com/)

### Instalação

#### 1. Clone o repositório

```bash
git clone https://github.com/seu-org/retratos-de-bonito.git
cd retratos-de-bonito
```

#### 2. Inicie o backend (FastAPI)

**Windows:**
```batch
run_back.bat
```

**Linux/Mac:**
```bash
# Ativar ambiente virtual
source .venv/bin/activate

# Instalar dependências (primeira vez)
pip install -r requirements.txt

# Rodar servidor
python -m uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000
```

**Backend rodando em:** http://localhost:8000/docs

#### 3. Inicie o frontend (Next.js)

Em outro terminal:

**Windows:**
```batch
run_front.bat
```

**Linux/Mac:**
```bash
cd src/frontend

# Instalar dependências (primeira vez)
npm install

# Rodar servidor
npm run dev
```

**Frontend rodando em:** http://localhost:3000

---

## 🎯 Funcionalidades Principais

### 1. 📅 Timeline Pública por Década

- Fotos agrupadas cronologicamente (1950s, 1960s, etc.)
- Acesso sem necessidade de login
- Apenas fotos públicas e validadas aparecem
- Navegação intuitiva e responsiva

### 2. 🔍 Busca Avançada

- Filtros: texto livre, pessoas, ano, local, eventos
- Resultados respeitam visibilidade e consentimento
- API pública em `/public/search`
- Sem tracking ou coleta de dados pessoais

### 3. 📸 Upload Comunitário

- Fluxo em 3 etapas acolhedoras (foto → metadados → obrigado)
- Metadados opcionais (data, local, pessoas)
- **Curadoria manual** antes de publicação (previne spam/conteúdo inadequado)
- Notificação de status (pendente → validada/rejeitada)

### 4. 🎥 Modo Exposição

- Timeline fullscreen para museus e eventos
- **Ken Burns effect** (zoom + pan suave em fotos)
- QR codes temáticos para exposições específicas
- Transições fade elegantes
- Ideal para projeção ou kiosk

[Veja documentação completa](src/frontend/EXPO.md)

### 5. 🔒 Gestão de Consentimento

- Registro de consentimento verbal/escrito/público
- Pessoas só aparecem em buscas públicas se consentirem
- Dashboard mostra status de consent por pessoa
- **Direito ao esquecimento**: revogação a qualquer momento

### 6. 📖 Histórias Orais

- Depoimentos textuais vinculados a fotos
- Controle de visibilidade (público/restrito/privado)
- Preserva contexto e memória oral
- Múltiplas histórias por foto (perspectivas diferentes)

### 7. 👥 Autenticação e Papéis (RBAC)

- **Usuário**: Contribuir fotos, visualizar públicas
- **Curador**: Validar/rejeitar fotos, gerenciar consentimento
- **Admin**: Acesso total, gestão de usuários
- JWT com expiração configurável

---

## 🏗️ Arquitetura do Sistema

### Stack Tecnológico

**Backend**:
- **FastAPI** (Python 3.10+) — API REST assíncrona
- **SQLAlchemy** — ORM com relacionamentos complexos
- **SQLite** (dev) / **PostgreSQL** (produção recomendada)
- **Alembic** — Migrations versionadas
- **JWT** — Autenticação stateless
- **Pydantic** — Validação de dados type-safe
- **Bcrypt** — Hash de senhas

**Frontend**:
- **Next.js 14** — React framework com App Router
- **TypeScript** — Type safety no client
- **Tailwind CSS** — Design system utilitário
- **Framer Motion** — Animações fluidas
- **React Context** — Gestão de estado de autenticação

**Armazenamento**:
- **Filesystem** — Fotos organizadas por ano/mês (`storage/YYYY/MM/`)
- **SHA256 hashing** — Deduplicação automática
- **Extensão futura**: S3-compatible (AWS S3, MinIO, Backblaze B2)

### Estrutura de Pastas

```
retratos-de-bonito/
├── src/
│   ├── app/                    # Backend FastAPI
│   │   ├── main.py             # Entry point, CORS
│   │   ├── database.py         # SQLAlchemy engine
│   │   ├── config/             # Configurações (security, settings)
│   │   ├── dependencies/       # DB session, auth guards
│   │   ├── models/             # ORM (Photo, Person, User, Consent, etc.)
│   │   ├── repositories/       # Data access layer (privacy-aware queries)
│   │   ├── routers/            # Endpoints (auth, photos, public, consents)
│   │   ├── schemas/            # Pydantic (validação)
│   │   └── services/           # Business logic (storage, auth)
│   │
│   ├── frontend/               # Frontend Next.js
│   │   ├── app/                # Pages (App Router)
│   │   │   ├── page.tsx        # Home (Timeline)
│   │   │   ├── search/         # Busca pública
│   │   │   ├── photos/[id]/    # Detalhe de foto
│   │   │   ├── login/          # Autenticação
│   │   │   ├── dashboard/      # Área do usuário
│   │   │   ├── curadoria/      # Painel curador
│   │   │   ├── contribuir/     # Upload comunitário
│   │   │   └── expo/           # Modo exposição
│   │   ├── components/         # React components
│   │   ├── lib/                # API client, auth context
│   │   └── config/             # Configurações de exposições
│   │
│   ├── alembic/                # Database migrations
│   ├── docs/                   # Documentação técnica
│   └── frontend_static/        # Fallback HTML/JS vanilla
│
├── scripts/                    # Utilitários (testes, verificações)
├── storage/photos/             # Arquivos de imagem (YYYY/MM/)
├── alembic.ini                 # Alembic config
├── requirements.txt            # Python dependencies
├── run_back.bat / run.sh       # Scripts de inicialização
└── README.md                   # Este arquivo
```

---

## 🔐 Privacidade & Ética

### Princípios de Design

Este projeto implementa **privacy-by-design** (privacidade por design):

1. **Consentimento Explícito**: Pessoas só aparecem em buscas públicas se consentirem
2. **Minimização de Dados**: Coletamos apenas o essencial
3. **Rastreabilidade**: Audit log registra todas as mudanças
4. **Reversibilidade**: Consentimento pode ser revogado a qualquer momento
5. **Transparência**: Dados pessoais podem ser exportados/deletados

### Modelo de Consentimento

```python
# Pessoas só aparecem em API pública se:
1. Foto está VALIDADA (curada)
2. Foto tem visibilidade PUBLICA
3. Pessoa tem consent_type = PUBLICO
   OU não há registro de consentimento (opt-in implícito configurável)
```

**Tipos de Consentimento:**
- **VERBAL**: Consentimento oral registrado
- **ESCRITO**: Consentimento documentado em papel
- **PUBLICO**: Consentimento explícito para exposição pública

### Compliance LGPD

- ✅ **Direito ao esquecimento** (soft delete)
- ✅ **Consentimento rastreado** com data (`consent_date`)
- ✅ **Minimização de dados** (só coleta essencial)
- ✅ **Segurança** (bcrypt passwords, JWT)
- ✅ **Transparência** (audit log)
- ✅ **Portabilidade** (exportação de dados em JSON)

---

## 🛠️ Tecnologias

| Camada | Tecnologia | Versão | Propósito |
|--------|-----------|--------|-----------|
| **Backend** | FastAPI | 0.100+ | API REST assíncrona |
| | SQLAlchemy | 2.0+ | ORM |
| | Alembic | 1.12+ | Migrations |
| | Pydantic | 2.0+ | Validação |
| | Bcrypt | - | Hash de senhas |
| **Frontend** | Next.js | 14.x | React framework |
| | TypeScript | 5.x | Type safety |
| | Tailwind CSS | 3.x | Styling |
| | Framer Motion | 10.x | Animações |
| **Database** | SQLite | 3.x | Dev |
| | PostgreSQL | 14+ | Produção |
| **Storage** | Filesystem | - | Fotos locais |

---

## 📚 Documentação

### Documentação Principal

| Documento | Descrição |
|-----------|-----------|
| [Backend README](src/app/README.md) | Setup backend, rotas, desenvolvimento |
| [Frontend README](src/frontend/README.md) | Setup frontend, componentes, build |
| [API Documentation](src/DOCS.md) | Referência completa de endpoints |
| [Metodologia](src/docs/metodologia.md) | Metodologia do projeto |

### Funcionalidades Especiais

| Documento | Descrição |
|-----------|-----------|
| [Modo Exposição](src/frontend/EXPO.md) | Timeline imersiva para museus |
| [QR Temático](src/frontend/QR_TEMATICO.md) | QR codes para exposições |
| [Fluxo de Contribuição](src/frontend/CONTRIBUICAO.md) | Upload comunitário |
| [Exemplos de Temas](src/frontend/EXEMPLOS_TEMA.md) | Exposições temáticas |

---

## 🧪 Scripts de Execução

### Scripts Disponíveis

| Script | Propósito | Quando Usar |
|--------|-----------|-------------|
| **`run_back.bat`** (Windows) | Inicia backend FastAPI | Desenvolvimento diário |
| **`run_front.bat`** (Windows) | Inicia frontend Next.js | Desenvolvimento diário |
| **`run.sh`** (Linux/Mac) | Inicia ambos (backend + frontend) | Desenvolvimento diário |
| **`test_back.bat`** | Testes backend | Validação manual |

### Modo Automático vs. Manual

**Modo Automático (Recomendado):**
- Valida pré-requisitos (.env, Node.js, venv)
- Mata processos antigos automaticamente
- Instala dependências se necessário
- Ideal para primeiro uso

```batch
# Windows
run_back.bat      # Terminal 1
run_front.bat     # Terminal 2
```

**Modo Manual (Avançado):**
- Controle total sobre flags
- Debugging detalhado
- Customização de parâmetros
- Ideal para desenvolvimento avançado

```bash
# Backend com debug
source .venv/bin/activate
export LOG_LEVEL=DEBUG
uvicorn src.app.main:app --reload --log-level debug

# Frontend com análise de bundle
cd src/frontend
ANALYZE=true npm run build
npm run dev
```

---

## 🐛 Troubleshooting

### Problemas Comuns

#### ❌ "npm não é reconhecido"
**Causa**: Node.js não instalado ou não está no PATH
**Solução**:
1. Instale Node.js: https://nodejs.org/
2. Reinicie o terminal
3. Verifique: `node --version`

#### ❌ "No module named 'fastapi'"
**Causa**: Dependências não instaladas no venv
**Solução**:
```batch
# Windows
.venv\Scripts\activate.bat
pip install -r requirements.txt

# Linux/Mac
source .venv/bin/activate
pip install -r requirements.txt
```

#### ❌ "Port 8000 already in use"
**Causa**: Servidor já rodando
**Solução**:
```batch
# Windows
netstat -ano | findstr :8000
taskkill /PID <número> /F

# Linux/Mac
lsof -ti:8000 | xargs kill -9
```

#### ❌ Frontend retorna 404 em rotas
**Causa**: Build de produção sem configuração de rewrites
**Solução**: Use `npm run dev` para desenvolvimento ou configure nginx/Vercel para produção

#### ❌ CORS errors no frontend
**Causa**: Backend não permite origem do frontend
**Solução**: Verifique `src/app/main.py` → `allow_origins` inclui `http://localhost:3000`

---

## 🤝 Como Contribuir

Contribuições são bem-vindas! Este projeto tem valor cultural e social.

### Formas de Contribuir

- 🐛 **Reportar bugs** via Issues
- 💡 **Sugerir funcionalidades** (especialmente relacionadas a ética/privacidade)
- 📝 **Melhorar documentação**
- 🧪 **Adicionar testes**
- 🎨 **Design e UX**
- 🌍 **Tradução** (i18n)

### Workflow

1. **Fork** o repositório
2. **Clone** seu fork: `git clone https://github.com/seu-usuario/retratos-de-bonito.git`
3. **Crie branch**: `git checkout -b feature/nome-da-feature`
4. **Desenvolva** seguindo padrões do projeto
5. **Teste** localmente
6. **Commit** com mensagens claras (Conventional Commits)
7. **Push** para seu fork
8. **Abra Pull Request** para `main`

### Padrões de Código

**Backend (Python)**:
- Seguir PEP 8
- Type hints obrigatórios
- Docstrings em funções públicas
- Validação com Pydantic

**Frontend (TypeScript)**:
- ESLint + Prettier configurados
- Componentes funcionais com hooks
- Props tipadas (TypeScript)
- Acessibilidade (ARIA labels)

**Convenção de Commits:**
```
<tipo>: <descrição curta>

feat: add consent revocation endpoint
fix: correct timeline grouping by decade
docs: update API reference
```

---

## 📜 Licença

Este projeto está licenciado sob **MIT License** para código e **Creative Commons BY-SA 4.0** para conteúdo.

- **Código-fonte**: MIT (livre para uso, inclusive comercial)
- **Conteúdo (fotos, docs)**: CC BY-SA 4.0 (atribuição + compartilhamento igual)

Ver [LICENSE](LICENSE) para detalhes.

---

## 🙏 Agradecimentos

- Comunidade de Bonito-MS pela confiança no projeto
- Contribuidores de código e conteúdo
- Instituições parceiras

---

## 📞 Contato & Suporte

- **GitHub Issues**: Para bugs e sugestões técnicas
- **Localização**: Bonito, Mato Grosso do Sul, Brasil

---

## 🗺️ Roadmap Futuro

### Curto Prazo (3 meses)
- [ ] Dockerização completa (backend + frontend + PostgreSQL)
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Testes automatizados (pytest + Jest)
- [ ] Deploy em staging

### Médio Prazo (6 meses)
- [ ] Migração SQLite → PostgreSQL
- [ ] Storage externo (S3-compatible)
- [ ] Internacionalização (i18n)
- [ ] Mobile app (React Native ou PWA)

### Longo Prazo (1 ano)
- [ ] Reconhecimento facial ético (sugestão de duplicatas)
- [ ] API GraphQL para clientes externos
- [ ] Guia de replicabilidade para outras comunidades

---

<div align="center">

**Retratos de Bonito — Preservando memórias, celebrando pertencimento** 📸✨

[![Feito com ❤️ em Bonito-MS](https://img.shields.io/badge/Feito%20com%20%E2%9D%A4%EF%B8%8F%20em-Bonito--MS-blue)](https://github.com/seu-org/retratos-de-bonito)

</div>
