# 🎨 Frontend — Guia Completo

**Retratos de Bonito — Next.js + React**

Interface web moderna e responsiva para o acervo fotográfico.

---

## 🚀 Quick Start

### Requisitos
- Node.js 18+ ou npm 9+
- Backend rodando em http://localhost:8000

### Instalação

```bash
# Entrar na pasta do frontend
cd src/frontend

# Instalar dependências
npm install

# Configurar variáveis de ambiente
cp .env.example .env.local
# Editar .env.local conforme sua setup
```

### Rodar em Desenvolvimento

```bash
npm run dev
```

**O frontend estará em:** http://localhost:3000

### Build para Produção

```bash
npm run build
npm start
```

---

## 📋 Variáveis de Ambiente

Crie `.env.local` na raiz do `src/frontend/`:

```env
# API Backend
NEXT_PUBLIC_API_URL=http://localhost:8000

# URL do site (para QR codes)
NEXT_PUBLIC_SITE_URL=http://localhost:3000

# Produção (Vercel)
# NEXT_PUBLIC_API_URL=https://api.retratosdebonito.org
# NEXT_PUBLIC_SITE_URL=https://retratosdebonito.org
```

---

## 📁 Estrutura

```
src/frontend/
├── app/                       # Next.js App Router
│   ├── page.tsx               # Home (Timeline)
│   ├── layout.tsx             # Layout global
│   ├── photos/                # Detalhe da foto
│   │   └── [id]/page.tsx
│   ├── search/                # Busca
│   │   └── page.tsx
│   ├── expo/                  # 🎥 Modo Exposição
│   │   ├── page.tsx           # Telão
│   │   ├── [slug]/page.tsx    # Tema específico
│   │   └── layout.tsx
│   ├── contribuir/            # 📥 Upload comunitário
│   │   ├── page.tsx           # Landing
│   │   ├── foto/page.tsx      # 3 etapas
│   │   └── obrigado/page.tsx  # Confirmação
│   └── globals.css            # Estilos globais
├── components/                # React components
│   ├── Header.tsx
│   ├── Timeline.tsx
│   ├── ExpoThemeQRCode.tsx
│   └── ...
├── config/                    # Configurações
│   └── exposicoes.ts          # Temas de exposição
├── lib/                       # Utilitários
│   ├── api.ts                 # Fetch helpers
│   └── types.ts               # TypeScript types
├── types/                     # Tipos reutilizáveis
│   └── index.ts
├── public/                    # Assets estáticos
├── package.json
├── tsconfig.json
├── tailwind.config.ts
└── README.md                  # Este arquivo
```

---

## 🔧 Scripts Disponíveis

```bash
# Desenvolvimento
npm run dev                     # Inicia servidor dev (port 3000)

# Build
npm run build                   # Cria build otimizado
npm start                       # Roda build em produção

# Lint
npm run lint                    # Verifica código
```

---

## 📄 Páginas Principais

### 1. Home (`/`)
- Timeline organizada por década
- Cards de fotos com hover suave
- Link para cada foto

### 2. Detalhe da Foto (`/photos/[id]`)
- Imagem grande centralizada
- Descrição completa
- Pessoas retratadas (com reconhecimento)
- Histórias/depoimentos relacionados
- Button de download com termo

### 3. Busca (`/search`)
- Busca por descrição
- Filtro por local
- Filtro por período
- Resultados em grid

### 4. Modo Exposição (`/expo`)
- Timeline imersiva em tela cheia
- Ken Burns effect
- QR codes temáticos
- Auto-play com timing narrativo
- Indicador de progresso

### 5. Tema Específico (`/expo/[slug]`)
- Landing de tema (ex: `/expo/decadas-de-bonito`)
- Lista de fotos relacionadas
- SEO otimizado

### 6. Contribuição (`/contribuir`)
- **Landing:** Por que contribuir
- **Upload:** 3 etapas acolhedoras
- **Obrigado:** Confirmação e próximas etapas

---

## 🎨 Design & Paleta de Cores

### Cores Principales

```
Verde escuro:   #1F3D2B  (natureza)
Areia/Off-white: #F5F3EE  (papel)
Grafite:        #1C1C1C  (títulos)
Cinza quente:   #6B6B6B  (secundário)
```

### Tipografia

```
Títulos:  Playfair Display (serif, editorial)
Texto:    Inter (sans-serif, leitura)
```

### Componentes

- **Cards:** cantos 12-16px, shadow leve, hover sutil
- **Botões:** bg-verde, hover elevado, transição smooth
- **Inputs:** border claro, focus com outline verde
- **Modals:** fundo semi-opaco, centro, fade-in

---

## 🔌 API Integration

### Helpers (`lib/api.ts`)

```typescript
export async function getTimeline()
export async function searchPhotos(params: string)
export async function getPhotoDetail(id: string)
export async function getPhotoStories(id: string)
```

### Uso

```typescript
import { getTimeline } from '@/lib/api'

const timeline = await getTimeline()
```

---

## 🎥 Modo Exposição

### Features
- Timeline automática com timing narrativo
- 7s intro + 12s por foto
- Ken Burns effect suave (scale 1→1.05)
- QR code temático (canto inferior-direito)
- Controles mínimos (play/pause, contador)
- Indicador de progresso (barra topo)

### Temas (Configurável)

Em `config/exposicoes.ts`:

```typescript
export const exposicoes = {
  decadas: { slug: "decadas-de-bonito", ... },
  praca: { slug: "praca-central", ... },
  trabalho: { slug: "memoria-do-trabalho", ... },
  festas: { slug: "festas-celebracoes", ... }
}
```

Docs: [EXPO.md](EXPO.md)

---

## 📥 Fluxo de Contribuição

### 3 Etapas

1. **Upload da Foto**
   - Validação (tipo, tamanho)
   - Preview
   
2. **Contexto**
   - Descrição (obrigatória)
   - Origem (opcional)

3. **Consentimento**
   - Review
   - Checkbox ético
   - Envio

### Estados

```
/contribuir          → Landing (por que contribuir)
/contribuir/foto     → 3 etapas (upload)
/contribuir/obrigado → Confirmação (o que vem a seguir)
```

Docs: [CONTRIBUICAO.md](CONTRIBUICAO.md)

---

## 🔐 Segurança

### Validações Frontend

```typescript
// Tipo de arquivo
if (!file.type.startsWith('image/')) { ... }

// Tamanho
if (file.size > 10 * 1024 * 1024) { ... }

// Consentimento obrigatório
if (!accepted) { buttonDisabled = true }
```

### Sem Armazenamento Local

- Imagens não são salvas no browser
- Enviadas direto para backend
- Backend valida hash (duplicata)
- Backend valida malware

---

## 📦 Dependências Principais

```json
{
  "next": "14",
  "react": "18.2.0",
  "react-dom": "18.2.0",
  "framer-motion": "^10.16.18",
  "qrcode.react": "^1.0.1",
  "tailwindcss": "^3.x"
}
```

---

## 🧪 Testes (Futuro)

```bash
npm run test
npm run test:watch
npm run test:coverage
```

---

## 🚀 Deployment

### Vercel (Recomendado)

```bash
npm i -g vercel
vercel
```

**Env vars no Vercel Dashboard:**
```
NEXT_PUBLIC_API_URL = https://api.retratosdebonito.org
NEXT_PUBLIC_SITE_URL = https://retratosdebonito.org
```

### Docker

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "start"]
```

---

## 🔧 Troubleshooting

### Frontend não abre
```bash
# Verificar se porta 3000 está livre
netstat -ano | findstr :3000  # Windows
lsof -i :3000                  # Mac/Linux

# Tentar outra porta
npm run dev -- -p 3001
```

### API não conecta
```
- Verificar se backend está rodando (port 8000)
- Verificar NEXT_PUBLIC_API_URL em .env.local
- Verificar CORS no backend
```

### Build falha
```bash
# Limpar cache
rm -rf .next
npm install
npm run build
```

### Imagens não carregam
```
- Verificar se /storage/photos existe no backend
- Verificar NEXT_PUBLIC_API_URL
- Abrir browser DevTools (F12) → Network
```

---

## 📖 Documentação Adicional

- [Modo Exposição](EXPO.md)
- [QR Temático](QR_TEMATICO.md)
- [Fluxo de Contribuição](CONTRIBUICAO.md)
- [Design System](../DOCS.md)

---

## 🧠 Desenvolvimento

### Code Style

```typescript
// Use imports relativos
import { getTimeline } from '@/lib/api'

// Componentes em UPPERCASE
export default function MyComponent() { }

// Props com interfaces
interface MyComponentProps {
  title: string
  onClick: () => void
}

// Use async/await
const data = await fetch(...)
```

### Git Workflow

```bash
git checkout -b feature/nome-feature
git add .
git commit -m "feat: descrição"
git push origin feature/nome-feature
# Abra PR no GitHub
```

---

<div align="center">

**Frontend do Retratos de Bonito — Design silencioso, tecnologia moderna** 🎨✨

</div>
