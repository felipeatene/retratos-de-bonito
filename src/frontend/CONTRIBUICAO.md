# 📥 Fluxo de Inclusão de Imagens — Guia Completo

## O Conceito

Quem envia uma foto não está **"subindo arquivo"**.
Está **confiando uma memória**.

Portanto, o fluxo precisa:
- 🤝 Acolher
- 📖 Orientar
- 🔒 Proteger
- 😌 Não assustar

## Tipos de Inclusão

### 🔒 Inclusão Comunitária (Padrão)

- **Quem:** Qualquer pessoa
- **Status inicial:** Bruta (não processada)
- **Visibilidade:** Restrita (privada)
- **Publicação:** Manual (por curador)
- **Segurança:** Máxima

### 🧑‍🏫 Inclusão Curatorial (Futura)

- **Quem:** Você / coletivo curatorial
- **Status:** Pode vir mais completa
- **Publicação:** Ainda passa por validação
- **Caso de uso:** Acervos conhecidos, eventos organizados

**Decisão atual:** Começar com inclusão comunitária.

## Rotas e Páginas

| Rota | Página | Função |
|------|--------|--------|
| `/contribuir` | Landing de contribuição | Explica por que e como contribuir |
| `/contribuir/foto` | Upload em 3 etapas | Formulário acolhedor |
| `/contribuir/obrigado` | Confirmação | Fecha o ciclo emocional |

**Nada de `/upload`.** O nome importa culturalmente.

## UX em 3 Etapas

### Etapa 1 — A Fotografia

**O que acontece:**
- Escolher imagem (JPG, PNG, WebP)
- Preview grande
- Mensagem clara

**Mensagem ideal:**
> "Essa foto fará parte do acervo histórico de Bonito."

Nada técnico, nada assustador.

**Validações:**
- Tipo de arquivo (image/*)
- Tamanho máximo (10MB)
- Preview live
- Botão "Escolher outra imagem"

### Etapa 2 — Contexto Mínimo

**Campos:**
1. **Descrição** (obrigatório)
   - Texto livre
   - Placeholder: "Ex: Praça central nos anos 90, festa de Nossa Senhora..."
   - Sem limite de caracteres, mas 200+ recomendado

2. **Origem** (opcional)
   - Onde vem a foto
   - Exemplo: "arquivo pessoal", "acervo familiar", "jornal local"
   - Ajuda na curadoria

**O que não perguntamos:**
- Data exata (pode estar errada)
- Pessoas (curador valida depois)
- Localização precisa (evita doxxing)

### Etapa 3 — Consentimento + Confirmação

**O que aparece:**
- Resumo visual (foto + descrição + origem)
- Checkbox simples:

> ☑️ Confirmo que posso compartilhar esta imagem para fins culturais e históricos.

**Sem juridiquês pesado.**

**Após enviar:**
- Mensagem humana
- Explicação do que vem a seguir
- Links para explorar acervo ou enviar outra

## Componentes Implementados

### Página `/contribuir`

```tsx
// Introdução acolhedora
// "Como funciona" em 3 passos
// Por que importa (contexto cultural)
// CTA principal: "Enviar uma fotografia"
```

**Psicologia:** Antes de pedir, explique. Gera confiança.

### Página `/contribuir/foto`

```tsx
// Estado mental: foco, silêncio, cuidado

// Indicador de progresso (3 barras)
// Step-by-step navigation
// Validações inline
// Preview live
// Botões clara distinção entre ações
```

**Fluxo:**
1. Upload → Preview
2. Descrição + Origem
3. Review + Checkbox + Envio

### Página `/contribuir/obrigado`

```tsx
// Agradecimento genuíno
// "O que acontece agora?" (5 passos)
// Links para voltar ou explorar
// Email para suporte
```

**Importância:** Fecha o ciclo emocional. Pessoa deve se sentir **valorizada**, não descartada.

## Integração com Backend

O frontend:
- ✅ Usa endpoint `/photos/upload`
- ✅ Envia `file`, `description`, `source`
- ✅ Respeita `status = bruta`
- ✅ Respeita `visibility = restrita`
- ✅ Não tenta publicar nada sozinho
- ✅ Segurança máxima

**Seu backend já está pronto para isso.**

### Endpoint Esperado

```
POST /photos/upload
Content-Type: multipart/form-data

file: File (obrigatório)
description: string (obrigatório)
source: string (opcional)
```

**Resposta esperada:**
```json
{
  "status": "ok",
  "photo_id": 123,
  "message": "Foto recebida"
}
```

## Validações Frontend

| Campo | Validação | Mensagem |
|-------|-----------|----------|
| Arquivo | Tipo (image/*) | "Por favor, selecione uma imagem válida" |
| Arquivo | Tamanho (<10MB) | "A imagem deve ter menos de 10MB" |
| Descrição | Não vazio | Botão desabilitado |
| Consentimento | Checkbox obrigatório | Botão desabilitado |

## Fluxo Técnico

```
Visitante
  ↓
/contribuir (landing)
  ↓
"Enviar uma fotografia"
  ↓
/contribuir/foto (step 1: upload)
  ├─ Valida arquivo
  ├─ Mostra preview
  └─ "Continuar"
  ↓
/contribuir/foto (step 2: contexto)
  ├─ Campos: description, source
  └─ "Continuar"
  ↓
/contribuir/foto (step 3: consentimento)
  ├─ Resumo visual
  ├─ Checkbox de autorização
  └─ "Enviar fotografia"
  ↓
POST /photos/upload
  ├─ FormData: file, description, source
  └─ Validação backend
  ↓
/contribuir/obrigado
  ├─ Agradecimento
  ├─ "O que acontece agora?"
  └─ Links: explorar / enviar outra
```

## Segurança & Ética

### No Frontend
- ✅ Validação de tipo de arquivo
- ✅ Validação de tamanho
- ✅ Consentimento explícito
- ✅ Sem armazenamento local

### No Backend (seu código)
- ✅ Hash do arquivo (duplicatas)
- ✅ Status bruto (não publicado)
- ✅ Visibilidade restrita (privado)
- ✅ Quarentena de malware
- ✅ Metadados removidos
- ✅ Curadoria manual

## Comportamento Cultural Esperado

1. **Visitante curioso**
   - Lê `/contribuir`
   - Entende a importância
   - Se sente acolhido

2. **Clica em "Enviar fotografia"**
   - Fluxo é claro
   - Não é assustador
   - Progresso visível

3. **Envia a foto**
   - Sente que contribuiu
   - Não é abandonado
   - Sabe o que vem a seguir

4. **Volta ao acervo**
   - Ou envia outra
   - Ou compartilha com amigos
   - Comunidade cresce

## Casos de Uso Reais

### Dona Maria, 72 anos
```
Encontra foto antiga da praça
  ↓
Mostra para neta (técnica)
  ↓
Neta acessa /contribuir
  ↓
Enviam juntas (momento familiar)
  ↓
"Minha foto está na história de Bonito!"
```

### Prof. João (Escola)
```
Aula sobre história da cidade
  ↓
Alunos trazem fotos de avós
  ↓
Usam /contribuir na aula
  ↓
Projeto: "Bonito através dos anos"
```

### Evento Comunitário
```
Abertura de exposição
  ↓
QR: "Envie fotos antigas"
  ↓
Pessoas contribuem em tempo real
  ↓
Display ao vivo mostra novas fotos
```

## Roadmap Futuro

- [ ] Notificação por email quando publicada
- [ ] Galeria "Você contribuiu"
- [ ] Crédito automático ao publicar
- [ ] Histórias orais (áudio junto)
- [ ] Múltiplas fotos de uma vez
- [ ] API para parceiros (escolas, jornais)

## Mensagens-Chave

### Durante Upload
> "Essa fotografia fará parte do acervo histórico de Bonito."

### Durante Consentimento
> "Confirmo que posso compartilhar esta imagem para fins culturais e históricos."

### Página de Obrigado
> "Sua fotografia foi recebida com cuidado. Ela passará por curadoria e validação. Em breve, poderá fazer parte do acervo público."

---

**Conclusão:** Você não está pedindo arquivos. Está **convidando histórias visuais** com cuidado, respeito e transparência.

Isso gera confiança. Confiança gera comunidade. Comunidade cria memória.
