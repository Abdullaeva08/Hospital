"""
Скрипт для создания суперпользователя
"""
import os
import django

# Настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_project.settings')
django.setup()

from clinic.models import UserProfile

# Создаем суперпользователя
if not UserProfile.objects.filter(username='admin').exists():
    UserProfile.objects.create_superuser(
        username='admin',
        email='admin@hospital.ru',
        password='admin123',
        first_name='Администратор',
        last_name='Системы'
    )
    print('✅ Суперпользователь создан!')
    print('   Имя: admin')
    print('   Пароль: admin123')
else:
    print('⚠️  Суперпользователь уже существует')
