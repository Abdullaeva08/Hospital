# Скрипт для запуска Django сервера
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "🏥 Hospital - Запуск Django сервера" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📋 Данные для входа в админку:" -ForegroundColor Yellow
Write-Host "   URL:    http://127.0.0.1:8000/admin/" -ForegroundColor White
Write-Host "   Логин:  admin" -ForegroundColor White
Write-Host "   Пароль: admin123" -ForegroundColor White
Write-Host ""
Write-Host "Запускаем сервер..." -ForegroundColor Green
Write-Host ""

# Запуск сервера
.\venv\Scripts\python.exe manage.py runserver
