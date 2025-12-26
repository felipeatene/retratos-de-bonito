@echo off
REM Script unificado para rodar o projeto inteiro (Backend + Frontend)
REM Retratos de Bonito

setlocal enabledelayedexpansion

cd /d "%~dp0"

REM Tentar configurar terminal para UTF-8 (melhora exibição)
chcp 65001 >nul 2>&1

echo.
echo ====================================================
echo =   Retratos de Bonito — Startup Script
echo ====================================================
echo.

REM Verificar se .venv existe
if not exist ".venv" (
  echo Ambiente virtual não encontrado.
  echo Execute primeiro: python -m venv .venv
  pause
  exit /b 1
)

REM Ativar venv
echo Ativando ambiente virtual...
call .venv\Scripts\activate.bat >nul 2>&1

REM Configurar PYTHONPATH
set PYTHONPATH=src
echo PYTHONPATH configurado para: src/
echo.
REM Caminho absoluto do root do projeto (diretório deste script)
set ROOT=%~dp0

REM Iniciar backend em background
echo Iniciando Backend (FastAPI)...
start "Retratos de Bonito - Backend" /B python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000 --app-dir "%~dp0src"
timeout /t 2 /nobreak >nul

REM Pequena espera para o backend iniciar
timeout /t 2 /nobreak >nul
echo Se o backend nao responder em http://127.0.0.1:8000, verifique manualmente:
echo   PowerShell: Get-NetTCPConnection -LocalPort 8000
echo   CMD: netstat -ano ^| findstr ":8000"
echo Possiveis causas: porta em uso, firewall ou permissoes.
echo.

REM Iniciar frontend em background
echo Limpando possiveis servidores na porta 3000...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 3000 -ErrorAction SilentlyContinue | Select-Object -ExpandProperty OwningProcess -Unique | ForEach-Object { Try { Stop-Process -Id $_ -Force -ErrorAction SilentlyContinue } Catch {} }"

echo Iniciando Frontend (HTTP Server) em nova janela (visivel)...
start "Retratos de Bonito - Frontend" cmd /k "cd /d \"%~dp0src\frontend_static\" && python -m http.server 3000"
timeout /t 1 /nobreak >nul

echo.
echo ====================================================
echo =   PRONTO!
echo ====================================================
echo Backend (API):    http://127.0.0.1:8000
echo Swagger:          http://127.0.0.1:8000/docs
echo Frontend (Web):   http://127.0.0.1:3000
echo Busca:            http://127.0.0.1:3000/search.html
echo Banco de dados:   ./retratos.db
echo.
echo Para parar: Feche as janelas dos servidores ou pressione Ctrl+C nas janelas abertas.
echo.
