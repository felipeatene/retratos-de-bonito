#!/bin/bash
# Script unificado para rodar o projeto inteiro (Backend + Frontend)
# Retratos de Bonito

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "╔════════════════════════════════════════════════════╗"
echo "║     🏛️  Retratos de Bonito — Startup Script       ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Verificar se .venv existe
if [ ! -d ".venv" ]; then
  echo "❌ Ambiente virtual não encontrado."
  echo "   Execute primeiro: python -m venv .venv"
  exit 1
fi

# Ativar venv
echo "✓ Ativando ambiente virtual..."
source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate

# Configurar PYTHONPATH
export PYTHONPATH=src

echo "✓ PYTHONPATH configurado para: src/"
echo ""

# Iniciar backend em background
echo "🚀 Iniciando Backend (FastAPI)..."
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000 --app-dir src &
BACKEND_PID=$!
sleep 2

# Iniciar frontend em background
echo "🎨 Iniciando Frontend (HTTP Server)..."
python -m http.server 3000 --directory src/frontend_static &
FRONTEND_PID=$!
sleep 1

echo ""
echo "╔════════════════════════════════════════════════════╗"
echo "║                    ✅ PRONTO!                      ║"
echo "╠════════════════════════════════════════════════════╣"
echo "║                                                    ║"
echo "║  🔗 Backend (API):    http://127.0.0.1:8000       ║"
echo "║  📊 Swagger:          http://127.0.0.1:8000/docs  ║"
echo "║                                                    ║"
echo "║  🌐 Frontend (Web):   http://127.0.0.1:3000       ║"
echo "║  🔍 Busca:            http://127.0.0.1:3000/sear… ║"
echo "║                                                    ║"
echo "║  📁 Banco de dados:   ./retratos.db               ║"
echo "║                                                    ║"
echo "╠════════════════════════════════════════════════════╣"
echo "║  Para parar: Pressione Ctrl+C                      ║"
echo "║  Backend PID:  $BACKEND_PID                            ║"
echo "║  Frontend PID: $FRONTEND_PID                            ║"
echo "╚════════════════════════════════════════════════════╝"
echo ""

# Aguardar conclusão
wait
