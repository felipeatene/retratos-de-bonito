# 🎯 QR Code Temático — Guia Completo

## O Conceito

O QR Code representa a **exposição temática inteira**, não apenas o slide atual. Ele não muda a cada foto—representa o contexto narrativo completo.

**Exemplos de temas:**
- Décadas de Bonito
- Praça Central
- Memória do Trabalho
- Festas e Celebrações

## Onde Aparece

- ✅ Canto inferior-direito
- ✅ Em **todos** os slides de foto
- ✅ **Nunca** muda durante a exposição
- ❌ Não aparece em slides de década
- ❌ Não aparece em transições

**Tamanho:** 130px × 130px (escaneável a 2–4m)

**Texto:** "Explore esta exposição no seu celular"

## UX Correta

```
Telão mostrando série de fotos
  ├─ QR aponta para: /expo/decadas-de-bonito
  └─ Visitante:
     ├─ Observa a exposição (telão)
     ├─ Se curioso, saca celular
     ├─ Escaneia QR
     └─ Abre hub temático no navegador
        ├─ Lê contexto da exposição
        ├─ Explora fotos relacionadas
        └─ Aprofunda no próprio ritmo
```

**Diferença crucial:** O QR não leva para a foto individual, mas para o **contexto temático completo**.

## Diferença: QR Temático vs. QR de Foto

| Aspecto | QR Temático | QR de Foto |
|---------|----------|---------|
| Destino | `/expo/{slug}` | `/photos/{id}` |
| Mudança | Permanece igual | Muda a cada slide |
| Função | Exploração temática | Detalhe isolado |
| Contexto | Narrativa coletiva | Apenas a foto |
| Use em | Exposições longas | Galerias isoladas |

**Decisão no projeto:** Modo Exposição usa **QR Temático**.

## Configuração de Temas

Temas são definidos em `config/exposicoes.ts`:

```typescript
export const exposicoes = {
  decadas: {
    slug: "decadas-de-bonito",
    title: "Décadas de Bonito",
    description: "Uma viagem visual pelas transformações...",
    apiEndpoint: "/public/timeline"
  },

  praca: {
    slug: "praca-central",
    title: "Praça Central",
    description: "Registros históricos da Praça...",
    apiEndpoint: "/public/search?location=Praça"
  },

  trabalho: {
    slug: "memoria-do-trabalho",
    title: "Memória do Trabalho",
    description: "Fotografias que documentam o trabalho...",
    apiEndpoint: "/public/search?collection=trabalho"
  },

  festas: {
    slug: "festas-celebracoes",
    title: "Festas e Celebrações",
    description: "Momentos de alegria compartilhada...",
    apiEndpoint: "/public/search?collection=festas"
  }
}
```

**Vantagens:**
- Trocar/adicionar temas sem mexer em código complexo
- Curadoria simples via JSON
- Versionamento fácil via git
- Sem banco de dados extra

## Página Pública do Tema

Quando alguém scaneia o QR, chega em `/expo/{slug}`:

```
/expo/decadas-de-bonito
```

Essa página:
- Exibe o título e descrição da exposição
- Lista as fotos relacionadas (formato depende da resposta da API)
- Permite navegação livre
- Mantém todas as regras de privacidade
- É indexada por SEO (meta tags automáticas)

## Segurança e Ética

O QR aponta apenas para exposições **públicas e validadas**:

- ✅ Tema curado e publicado
- ✅ Fotos relacionadas com consentimento
- ✅ Conformidade com políticas de privacidade
- ❌ Dados restritos não são expostos

O QR respeita exatamente as mesmas regras de visibilidade da API `/public`.

## Componentes Implementados

### ExpoThemeQRCode.tsx

```tsx
export default function ExpoThemeQRCode({ 
  slug, 
  label = "Explore esta exposição no seu celular" 
}) {
  // Gera QR apontando para /expo/{slug}
}
```

**Props:**
- `slug: string` — slug do tema
- `label?: string` — texto abaixo do QR

### Uso na Exposição

```tsx
import { exposicoes } from '@/config/exposicoes'
import ExpoThemeQRCode from '@/components/ExpoThemeQRCode'

const tema = exposicoes.decadas

// No JSX:
<ExpoThemeQRCode slug={tema.slug} label="Explore esta exposição no seu celular" />
```

## Comportamento Cultural Esperado

Durante a exposição:

1. **Telão roda continuamente** — capítulos, décadas, fotos
2. **Visitante observa** — contempla a narrativa coletiva
3. **Se curioso, scaneia** — QR convida, não obriga
4. **Abre no celular** — hub temático com contexto completo
5. **Explora no próprio ritmo** — aprofunda a curiosidade
6. **Telão continua** — não depende de ninguém
7. **Duas camadas de experiência** — sem conflito

## Casos de Uso

### Museu (8h/dia)

```
08:00 — Inicia exposição "Décadas de Bonito"
08:00–17:00 — Telão roda continuamente
10:30 — Visitante scaneia QR
10:30–11:00 — Explora /expo/decadas-de-bonito
11:00 — Volta a observar telão ou sai
```

### Escola

```
Professora abre exposição "Praça Central"
↓
Estudantes contemplam 20 min
↓
Alguns scaneia o QR
↓
Aprofundam em /expo/praca-central
↓
Discutem em roda
```

### Evento Comunitário

```
Abertura de evento: exibe "Festas e Celebrações"
↓
Pessoas reconhecem suas famílias nas fotos
↓
Scaneia QR para compartilhar no WhatsApp
↓
Convida amigos/parentes para ver também
```

## Teste Prático

Antes de usar em evento real:

- [ ] Teste leitura a 2m
- [ ] Teste leitura a 3m
- [ ] Teste leitura a 4m
- [ ] Teste com luz forte (janela, projetor)
- [ ] Teste com luz baixa (à noite)
- [ ] Teste com Android
- [ ] Teste com iOS
- [ ] Teste URL: `/expo/{slug}` abre corretamente
- [ ] Confirma que fotos carregam na página temática

Se não ler em 4m → aumente o QR de 130px para 150–160px.

## Roadmap

- [ ] Suporte para múltiplos temas na mesma exposição (seletor)
- [ ] Analytics: quantos QRs escaneados, tempo médio na página
- [ ] Histórias ampliadas por tema (depoimentos orais)
- [ ] Integração com Telegram/WhatsApp (compartilhamento)
- [ ] Modo offline (service worker)

## Leitura Cultural

O QR temático:

- **Transforma espectadores em pesquisadores** — convida exploração
- **Leva memória para o bolso** — acesso contínuo via celular
- **Conecta gerações** — avós mostram para netos
- **Respeita o tempo de cada um** — sem pressa
- **Cria ponte** — espaço público ↔ arquivo digital

Você não criou apenas um QR.

Você criou um **portal entre dimensões da memória**.
