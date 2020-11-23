REM Setups a python virutal environment with dependencies installed.
@echo off

call deactivate 2>nul
ver >nul

if not exist venv (
    echo Creating venv
    python -mvenv venv
)

call venv\scripts\activate

pip install -r requirements.txt

set PYTHONPATH=%~dp0\src