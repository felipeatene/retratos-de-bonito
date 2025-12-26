@echo off
REM ============================================================
REM Retratos de Bonito — Backend (FastAPI)
REM ============================================================
REM Este script inicia a API em http://localhost:8000

cd /d %~dp0

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ❌ Python não encontrado!
    echo.
    echo Por favor, instale Python 3.10+ em:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Criar ambiente virtual se não existir
if not exist "venv" (
    echo.
    echo Criando ambiente virtual...
    echo.
    python -m venv venv
)

REM Ativar ambiente virtual
call venv\Scripts\activate.bat

REM Instalar requirements
echo.
echo Verificando dependências...
echo.
python -m pip install --quiet -r requirements.txt
if errorlevel 1 (
    echo.
    echo ❌ Erro ao instalar dependências
    pause
    exit /b 1
)

REM Configurar PYTHONPATH para src/
set PYTHONPATH=%cd%\src

REM Rodar o servidor
echo.
echo ============================================================
echo 🔧 Iniciando Backend (FastAPI)
echo ============================================================
echo.
echo URL: http://localhost:8000
echo Docs: http://localhost:8000/docs
echo.
echo Pressione Ctrl+C para parar
echo.

python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause
