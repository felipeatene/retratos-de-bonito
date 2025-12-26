@echo off
REM ============================================================
REM Teste Rápido — Backend Retratos de Bonito
REM ============================================================

cd /d %~dp0

echo.
echo ============================================================
echo 🧪 Testando Backend
echo ============================================================
echo.

REM Ativar venv e testar
call venv\Scripts\activate.bat

echo [1/3] Testando importação do FastAPI...
python test_backend.py
if errorlevel 1 (
    echo.
    echo ❌ Erro ao carregar aplicação
    pause
    exit /b 1
)

echo.
echo [2/3] Iniciando servidor FastAPI...
echo.
echo 📍 URL: http://localhost:8000
echo 📚 Docs: http://localhost:8000/docs
echo.
echo Pressione Ctrl+C para parar
echo.

set PYTHONPATH=%cd%\src
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
