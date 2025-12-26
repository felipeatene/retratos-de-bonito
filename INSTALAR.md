# 🚀 Guia de Instalação — Retratos de Bonito

## ⚠️ O que você precisa instalar ANTES

### 1. Python 3.10+
✅ **JÁ INSTALADO** — Python 3.14.2 detectado

### 2. Node.js 18+ (NECESSÁRIO)
❌ **NÃO INSTALADO** 

**Baixe e instale aqui**: https://nodejs.org/

- Escolha a versão **LTS (Long Term Support)**
- Durante a instalação, marque a opção: **"Add to PATH"**
- Após instalar, **reinicie o terminal**

---

## 📋 Como rodar o projeto

### Opção 1: Scripts Automáticos (.bat)

Após instalar Node.js:

```batch
# Terminal 1 — Backend
run_back.bat

# Terminal 2 — Frontend (em outra janela)
run_front.bat
```

### Opção 2: Manual (passo a passo)

#### Backend (FastAPI)

```batch
# Ativar ambiente virtual
venv\Scripts\activate.bat

# Instalar dependências (só na primeira vez)
pip install -r requirements.txt

# Rodar servidor
python -m uvicorn src.app.main:app --reload --host 0.0.0.0 --port 8000
```

**URL**: http://localhost:8000/docs

#### Frontend (Next.js)

```batch
cd src\frontend

# Instalar dependências (só na primeira vez)
npm install

# Rodar servidor
npm run dev
```

**URL**: http://localhost:3000

---

## 🐛 Problemas Comuns

### ❌ "npm não é reconhecido"
→ Node.js não está instalado ou não está no PATH
→ **Solução**: Instale Node.js e reinicie o terminal

### ❌ "No module named 'fastapi'"
→ Dependências não foram instaladas no venv
→ **Solução**: 
```batch
venv\Scripts\activate.bat
pip install -r requirements.txt
```

### ❌ "Port 8000 already in use"
→ Já existe um servidor rodando
→ **Solução**: 
```batch
# Encontrar processo
netstat -ano | findstr :8000

# Matar processo (substitua PID)
taskkill /PID <número> /F
```

---

## ✅ Como saber se está funcionando

### Backend ✓
- Abra: http://localhost:8000/docs
- Você deve ver a documentação Swagger da API

### Frontend ✓
- Abra: http://localhost:3000
- Você deve ver a página inicial com timeline de fotos

---

## 📞 Precisa de ajuda?

1. Verifique que Node.js está instalado: `node --version`
2. Verifique que Python está instalado: `python --version`
3. Consulte [src/app/README.md](src/app/README.md) para detalhes do backend
4. Consulte [src/frontend/README.md](src/frontend/README.md) para detalhes do frontend
