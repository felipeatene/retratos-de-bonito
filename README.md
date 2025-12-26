<div align="center">

# 🌿📸 Retratos de Bonito 💧

### Acervo Fotográfico Cultural • Memória • Identidade • Pertencimento

Preservação da memória visual de Bonito (MS),  
com acesso seguro, consentido e uso ético da tecnologia.

</div>

---

## 🚀 Quickstart

### Windows
```cmd
run.bat
```

### Linux / Mac
```bash
bash run.sh
```

Acesse:
- **Frontend:** http://127.0.0.1:3000
- **API:** http://127.0.0.1:8000
- **Docs:** http://127.0.0.1:8000/docs

### 🖥️ Modo Exposição
- **URL:** http://127.0.0.1:3000/expo
- **Fonte de dados:** GET /public/expo?mode=timeline
- **Config:** defina `NEXT_PUBLIC_API_URL` apontando para a API (ex.: `http://127.0.0.1:8000`)

---

## 📁 Estrutura do Projeto

```
src/
├── app/                       # FastAPI Backend
│   ├── main.py               # Entry point
│   ├── database.py           # SQLite + SQLAlchemy
│   ├── models/               # ORM (Photo, Person, Story, etc)
│   ├── schemas/              # Pydantic schemas
│   ├── repositories/         # Camada de dados
│   ├── services/             # Lógica de negócio
│   └── routers/              # Endpoints
├── alembic/                  # Migrações de BD
├── frontend_static/          # Frontend (HTML + JS estático)
│   ├── index.html            # Timeline
│   ├── search.html           # Busca pública
│   ├── photo.html            # Detalhe + histórias
│   └── api.js                # Helpers de fetch
└── README.md

scripts/                       # Utilitários (import, testes)
storage/                       # Fotos originais
retratos.db                    # Banco SQLite
```

---

## 🔗 Endpoints Principais

A partir desse cadastro, o sistema realiza a comparação entre as imagens de referência e o acervo fotográfico existente, possibilitando que cada usuário visualize fotografias em que aparece, respeitando critérios de privacidade e permissões de acesso.

O projeto também permite a inclusão colaborativa de fotografias, contribuindo para a ampliação e diversificação do acervo histórico da cidade.

---

## 4. Privacidade, Ética e Consentimento

O **Retratos de Bonito** adota princípios rigorosos de proteção de dados e respeito à privacidade, especialmente no que se refere a informações biométricas.

As diretrizes fundamentais incluem:
- Uso de reconhecimento facial exclusivamente mediante consentimento explícito
- Tratamento de dados biométricos como informações sensíveis
- Ausência de disponibilização pública irrestrita de imagens
- Controle de acesso às fotografias com base em permissões
- Possibilidade de exclusão de dados mediante solicitação do usuário

O projeto está alinhado aos princípios da legislação brasileira de proteção de dados pessoais (LGPD) e às boas práticas de ética digital.

Mais informações podem ser encontradas na documentação específica em `docs/privacy.md`.

---

## 5. Caráter Cultural do Projeto

O **Retratos de Bonito** não se configura como uma rede social, plataforma de vigilância ou ferramenta de monitoramento.

Trata-se de um projeto de caráter cultural, histórico e comunitário, cujo foco é a preservação da memória coletiva, o fortalecimento da identidade local e o acesso consciente ao patrimônio visual da cidade.

---

## 6. Tecnologias Utilizadas

O projeto é desenvolvido utilizando tecnologias consolidadas e amplamente adotadas na comunidade de software:

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
