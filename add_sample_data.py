"""
Скрипт для добавления тестовых данных в базу
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_project.settings')
django.setup()

from clinic.models import Specialization, Doctor, Schedule

# Создаём специализации
specializations_data = [
    {'name': 'Кардиология', 'description': 'Диагностика и лечение заболеваний сердечно-сосудистой системы'},
    {'name': 'Терапия', 'description': 'Общая диагностика и лечение различных заболеваний'},
    {'name': 'Хирургия', 'description': 'Оперативное лечение различных заболеваний'},
    {'name': 'Неврология', 'description': 'Диагностика и лечение заболеваний нервной системы'},
    {'name': 'Педиатрия', 'description': 'Медицинская помощь детям от 0 до 18 лет'},
    {'name': 'Стоматология', 'description': 'Лечение и профилактика заболеваний полости рта'},
]

print('Создаём специализации...')
for spec_data in specializations_data:
    spec, created = Specialization.objects.get_or_create(
        name=spec_data['name'],
        defaults={'description': spec_data['description']}
    )
    if created:
        print(f'✓ Создана: {spec.name}')

# Создаём врачей
print('\nСоздаём врачей...')
cardiology = Specialization.objects.get(name='Кардиология')
therapy = Specialization.objects.get(name='Терапия')
surgery = Specialization.objects.get(name='Хирургия')

doctors_data = [
    {'first_name': 'Иван', 'last_name': 'Петров', 'patronymic': 'Сергеевич', 
     'specialization': cardiology, 'experience_years': 15, 'price': 2500},
    {'first_name': 'Мария', 'last_name': 'Смирнова', 'patronymic': 'Александровна', 
     'specialization': therapy, 'experience_years': 10, 'price': 2000},
    {'first_name': 'Алексей', 'last_name': 'Кузнецов', 'patronymic': 'Владимирович', 
     'specialization': surgery, 'experience_years': 20, 'price': 3500},
    {'first_name': 'Елена', 'last_name': 'Васильева', 'patronymic': 'Дмитриевна', 
     'specialization': cardiology, 'experience_years': 12, 'price': 2300},
    {'first_name': 'Сергей', 'last_name': 'Соколов', 'patronymic': 'Игоревич', 
     'specialization': therapy, 'experience_years': 8, 'price': 1800},
]

for doc_data in doctors_data:
    doc, created = Doctor.objects.get_or_create(
        first_name=doc_data['first_name'],
        last_name=doc_data['last_name'],
        defaults=doc_data
    )
    if created:
        print(f'✓ Создан: {doc}')
        
        # Создаём расписание для каждого врача
        Schedule.objects.get_or_create(
            doctor=doc, day_of_week='MON',
            defaults={'start_time': '09:00', 'end_time': '17:00'}
        )
        Schedule.objects.get_or_create(
            doctor=doc, day_of_week='WED',
            defaults={'start_time': '09:00', 'end_time': '17:00'}
        )
        Schedule.objects.get_or_create(
            doctor=doc, day_of_week='FRI',
            defaults={'start_time': '09:00', 'end_time': '17:00'}
        )

print('\n✅ Тестовые данные успешно добавлены!')
print('Запустите сервер: py manage.py runserver')
