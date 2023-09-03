@echo off

:: Ejecutar el comando Python en la primera ventana de cmd
start cmd /k python index.py

:: Esperar un poco antes de abrir la segunda ventana
ping -n 2 127.0.0.1 > nul

:: Abrir la segunda ventana y ubicarla en el mismo directorio
start cmd /k cd /d %~dp0
