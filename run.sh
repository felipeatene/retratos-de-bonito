#!/bin/bash
# Script para rodar o servidor FastAPI

echo "Setting PYTHONPATH..."
export PYTHONPATH=src

echo "Starting Retratos de Bonito API..."
echo ""
echo "Server running at: http://127.0.0.1:8000"
echo "Swagger UI: http://127.0.0.1:8000/docs"
echo ""

uvicorn app.main:app --reload --app-dir src
