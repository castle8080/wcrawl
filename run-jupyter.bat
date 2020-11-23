@echo off

REM move to app directory
cd %~dp0

call dev-environment.bat
jupyter lab