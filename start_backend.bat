@echo off
cd /d "%~dp0backend"

set "PYTHONPATH=./language"
python -m uvicorn API.apiConnection:mainAPI --reload

pause
