<div align="center">

# 🌿📸 Retratos de Bonito 💧

**Museu Digital Comunitário**

Preservação da memória visual de Bonito (MS) com acesso seguro, consentido e ético.

</div>

---

## 🚀 Início Rápido

### ⚠️ Pré-requisitos

1. ✅ **Python 3.10+** (você já tem instalado)
2. ❌ **Node.js 18+** — **[CLIQUE PARA INSTALAR](https://nodejs.org/)** (necessário para frontend)

### Modo Automático (Recomendado)

#### Windows
```cmd
# Terminal 1 — Backend (FastAPI)
run_back.bat

# Terminal 2 — Frontend (Next.js) — após instalar Node.js
run_front.bat
```

#### Linux / Mac
```bash
bash run.sh
```

Isso inicia:
- **Backend API:** http://localhost:8000/docs
- **Frontend:** http://localhost:3000

### Modo Manual (Desenvolvimento)

Veja instruções detalhadas em:
- **[INSTALAR.md](INSTALAR.md)** — Guia de instalação completo
- **[Backend — Guia de Setup](src/app/README.md)**
- **[Frontend — Guia de Setup](src/frontend/README.md)**

---

## 📁 Estrutura do Projeto

```
retratos-de-bonito/
├── src/
│   ├── app/                    # Backend FastAPI
│   │   ├── main.py
│   │   ├── models/             # ORM
│   │   ├── repositories/       # Acesso a dados
│   │   ├── routers/            # Endpoints
│   │   └── README.md           # 👈 Instruções backend
│   │
│   └── frontend/               # Frontend Next.js
│       ├── app/
│       ├── components/
│       ├── config/
│       └── README.md           # 👈 Instruções frontend
│
├── alembic/                    # Migrações BD
├── scripts/                    # Utilitários
├── storage/photos/             # Armazenamento de fotos
├── retratos.db                 # Banco de dados SQLite
└── README.md                   # Este arquivo
```

---

## 📖 Documentação

| Documento | Objetivo |
|-----------|----------|
| [Backend README](src/app/README.md) | Setup, rotas, desenvolvimento |
| [Frontend README](src/frontend/README.md) | Setup, componentes, build |
| [Guia de Modo Exposição](src/frontend/EXPO.md) | Visualização imersiva |
| [QR Temático](src/frontend/QR_TEMATICO.md) | Integração QR codes |
| [Fluxo de Contribuição](src/frontend/CONTRIBUICAO.md) | Upload comunitário |

---

## 🎯 Funcionalidades Principais

### 🔍 Busca Pública
- Busca por descrição, local, período
- Sem necessidade de login
- Resultados respeitam visibilidade

### 📷 Upload Comunitário
- 3 etapas acolhedoras
- Consentimento explícito
- Curadoria manual antes de publicar

### 🎥 Modo Exposição
- Timeline imersiva em tela cheia
- Ken Burns effect suave
- QR codes temáticos
- Ideal para museus, escolas, eventos

### 🔒 Privacidade & Ética
- Consentimento obrigatório
- Visibilidade controlada
- LGPD compliant
- Sem vigilância

---

## 🛠️ Tecnologias

**Backend:**
- Python 3.10+
- FastAPI
- SQLAlchemy + SQLite
- Pydantic

**Frontend:**
- React 18+
- Next.js 14
- Tailwind CSS
- Framer Motion (animações)

---

## 📞 Suporte

Dúvidas ou problemas?
- Abra uma issue no repositório
- Consulte a documentação específica
- Entre em contato pelo email do projeto

---

<div align="center">

**Retratos de Bonito — Preservando a memória de gerações** 📸✨

</div>


- Linguagem Python
- API REST com FastAPI
- Indexação vetorial para reconhecimento facial
- Banco de dados relacional (PostgreSQL ou SQLite)
- Armazenamento privado de arquivos
- Contêineres Docker para padronização do ambiente

---

## 7. Contribuições e Colaborações

O projeto está aberto à colaboração de fotógrafos, pesquisadores, historiadores, desenvolvedores e membros da comunidade interessados em contribuir para a preservação da memória cultural de Bonito.

Sugestões, contribuições técnicas e parcerias institucionais são bem-vindas.

---

## 8. Localização

**Bonito – Mato Grosso do Sul – Brasil**
