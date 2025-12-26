# 🎥 Modo Exposição — Documentação

## O Conceito

O **Modo Exposição** transforma o acervo de Retratos de Bonito em uma experiência imersiva de tela cheia, apropriada para:

- Museus e centros culturais (display contínuo)
- Escolas (aula histórica envolvente)
- Eventos comunitários (contexto visual)
- Pesquisa e contemplação (narrativa por época)

Cada década é apresentada como um **capítulo**, com:
- 1 slide de abertura (7 segundos)
- 3–6 fotos (12 segundos cada)
- Transições suaves (fade 1.5s)

## Arquitetura

### Estrutura de Slides

```typescript
type Slide =
  | { type: "intro"; decade: number }
  | { type: "photo"; photo: PhotoData }
```

### Fluxo de Dados

```
API /public/timeline
    ↓
buildSlides() → array de Slide
    ↓
ExpoPage → AnimatePresence + transições
    ↓
Tela cheia (w-screen h-screen)
```

## Timing Ideal

| Tipo | Duração | Razão |
|------|---------|-------|
| Intro (texto) | 7s | Leitura + contemplação |
| Foto | 12s | Detalhes visíveis + Ken Burns |
| Fade out | 1.5s | Transição narrativa |

## Animações

### Ken Burns Effect (suave)

```
scale: 1 → 1.05 (12s)
easing: easeInOut
imperceptível ao olho
```

Isso cria **vida visual** sem roubar atenção.

### Transições Crossfade

```
opacity: 0 → 1 (1.2s)
modo: wait (una vez à vez)
sem slide lateral / bounce
```

## UX de Telão

### Visual

- ✅ Fundo preto absoluto (`bg-black`)
- ✅ Sem bordas, sombras ou elementos piscando
- ✅ Texto mínimo (2 linhas máx) na base
- ✅ Contraste alto (branco sobre gradiente escuro)

### Orientação Implícita

Em **3 segundos**, o visitante deve entender:
1. Está vendo um acervo histórico
2. De fotografias da cidade Bonito
3. Organizado por época

**Sem instruções verbais.**

## Funcionalidades

### Controles Mínimos

| Botão | Função | Visibilidade |
|-------|--------|--------------|
| ⏸ / ▶ | Pausar/Reproduzir | Canto inferior-direito |
| Contador | Slide atual / Total | Canto inferior-direito |
| Barra | Progresso do slide | Topo (fina, 2px) |

### Comportamento Robusto

- ✅ Sem reinício ao perder foco
- ✅ Funciona 24h contínuo
- ✅ Sem dependência de mouse
- ✅ Responsive em telas grandes

## Acessibilidade

- Descrições de imagem em aria-label
- Contraste AA em todos os textos
- Navegação por teclado (teclas de seta opcionais)
- Fonte legível (1.2–2rem)

## Desenvolvimento

### Instalar Dependências

```bash
npm install framer-motion qrcode.react
```

### Configurar Variáveis de Ambiente

Crie `.env.local` na raiz do frontend:

```
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_SITE_URL=http://localhost:3000
```

Em produção (Vercel/similar):

```
NEXT_PUBLIC_API_URL=https://api.retratosdebonito.org
NEXT_PUBLIC_SITE_URL=https://retratosdebonito.org
```

### Rodar Localmente

```bash
npm run dev
# Acessa http://localhost:3000/expo
```

### Build para Produção

```bash
npm run build
npm start
```

## Customização

### Mudar Duração de Slides

Em `app/expo/page.tsx`, ajuste:

```typescript
const duration = current.type === 'intro' ? 7000 : 12000
//                                           ↑         ↑
//                                         intro   photo
```

### Mudar Cores do Fundo

Substitua `bg-black` por qualquer cor (sugestão: `#0a0a0a` para suavidade).

### Desabilitar Ken Burns

Remova ou comente:

```typescript
animate={{ scale: 1.05 }}
```

## Performance

- Imagens carregadas em background (não bloqueiam transição)
- Fade suave sem flickering
- Timeout limpo para evitar memory leaks

## Integração com API

A página faz fetch de:

```
GET {API_BASE}/public/timeline
```

Resposta esperada:

```json
[
  {
    "decade": 1990,
    "photos": [
      {
        "photo_id": 1,
        "file_name": "path/to/image.jpg",
        "description": "Praça central",
        "location": "Centro",
        "original_date": "1995"
      }
    ]
  }
]
```

## QR Code Dinâmico

### Conceito

O QR Code aparece **discreetamente** no canto inferior direito de cada slide de foto. Ele não interrompe a contemplação, mas convida quem quiser saber mais a se aproximar do celular.

**Onde aparece:**
- ✅ Slides de foto (canto inferior-direito)
- ❌ Slides de década
- ❌ Transições

**Tamanho:** 120px × 120px (escaneável a 2–4m)

### UX Correta

```
Telão mostrando foto de 1995
  └─ Visitante observa
     └─ Quer saber mais
        └─ Saca celular
           └─ Escaneia QR
              └─ Abre /photos/{photo_id} no navegador
                 └─ Lê descrição completa, histórias, pessoas
```

O telão continua rodando. **Sem interrupção.**

### Segurança e Ética

O QR aponta apenas para fotos **validadas e públicas**:

- ✅ Foto marcada como pública
- ✅ Pessoas com consentimento
- ✅ Histórias liberadas
- ❌ Dados restritos não são expostos

O QR respeita exatamente as mesmas regras de visibilidade da página pública.

### Configuração

No arquivo `.env.local`:

```env
NEXT_PUBLIC_SITE_URL=https://seu-dominio.org
```

O componente `ExpoQRCode` gera URLs no formato:

```
https://seu-dominio.org/photos/{photo_id}
```

## Casos de Uso

### 1. Exposição Permanente em Museu

- Roda 8h/dia sem interrupção
- Visitantes passam e observam
- Sem barulho, só imagens

### 2. Aula Escolar

- Professor abre modo exposição
- Estudantes contemplam historia visual
- Depois discutem

### 3. Evento Comunitário

- Tela grande durante abertura
- Pessoas se veem nas fotos
- Gera engajamento natural

## Roadmap Futuro

- [ ] Sincronização multi-telas (para galerias com várias monitores)
- [ ] Seleção de período (usuário escolhe décadas específicas)
- [ ] Áudio ambiental (som de cidade, pássaros, vento)
- [ ] Histórias ampliadas em segundo QR (depoimentos orais)
- [ ] Controle via controle remoto (IR para eventos)
- [ ] Modo noturno (menor brilho para ambiente escuro)

## Referências Conceituais

Este design segue princípios de:

- **Ken Burns** (cinema documental)
- **Museum UX** (Guggenheim, MOMA)
- **Contemplative Computing** (tempo respeitado)
- **Silent Design** (interface invisível)

O resultado é uma **experiência cultural**, não uma apresentação.
