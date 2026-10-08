@echo off
chcp 65001 >nul
echo ========================================
echo 🏥 Hospital - Запуск Django сервера
echo ========================================
echo.
echo Запускаем сервер разработки...
echo.
venv\Scripts\python.exe manage.py runserver
