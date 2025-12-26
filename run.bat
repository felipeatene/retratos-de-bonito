@echo off
REM Script para rodar o servidor FastAPI
setlocal enabledelayedexpansion

echo Setting PYTHONPATH...
set PYTHONPATH=src

echo Starting Retratos de Bonito API...
echo.
echo Server running at: http://127.0.0.1:8000
echo Swagger UI: http://127.0.0.1:8000/docs
echo.

.venv\Scripts\uvicorn.exe app.main:app --reload --app-dir src
