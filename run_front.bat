@echo off
chcp 65001 >nul
REM ============================================================
REM Retratos de Bonito - Frontend (Next.js)
REM ============================================================

cd /d "%~dp0"
cd src\frontend

REM Adicionar Node.js ao PATH
set "PATH=C:\Program Files\nodejs;%PATH%"

REM Verificar npm
where npm >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Node.js/npm nao encontrado!
    echo Instale em: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

REM Instalar dependencias se necessario
if not exist "node_modules" (
    echo.
    echo Instalando dependencias...
    call npm install
)

REM Rodar servidor
echo.
echo ============================================================
echo Iniciando Frontend - Next.js
echo ============================================================
echo.
echo URL: http://localhost:3000
echo.
echo Pressione Ctrl+C para parar
echo.

call npm run dev

pause
