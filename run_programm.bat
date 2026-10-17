@echo off
set "PROJECT_DIR=%~dp0"

start "Backend" cmd /k "cd /d "%PROJECT_DIR%backend" && set "PYTHONPATH=./language" && python -m uvicorn API.apiConnection:mainAPI --reload"

start "React" cmd /k "cd /d "%PROJECT_DIR%frontend" && npm run dev -- --host localhost"

timeout /t 5 /nobreak >nul
start "" "http://localhost:5173"

