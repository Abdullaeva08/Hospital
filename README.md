# 🏥 Hospital — Учебный сайт медицинской клиники

Образовательный проект для изучения Django (models + базовая логика).

## 📋 Описание

Веб-сайт медицинской клиники, где пользователи могут:
- Регистрироваться как пациент
- Просматривать врачей по специализациям
- Записываться на приём
- Просматривать историю своих приёмов

## 🗂️ Структура проекта

```
Hospital/
├── hospital_project/       # Настройки Django проекта
│   ├── __init__.py
│   ├── settings.py         # Конфигурация проекта
│   ├── urls.py             # URL-маршруты
│   ├── wsgi.py
│   └── asgi.py
├── clinic/                 # Основное приложение
│   ├── migrations/         # Миграции базы данных
│   ├── __init__.py
│   ├── admin.py            # Настройка админ-панели
│   ├── apps.py
│   └── models.py           # Модели данных
├── media/                  # Загружаемые файлы
├── static/                 # Статические файлы
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Установка и запуск

### 1. Создать виртуальное окружение

```bash
python -m venv venv
```

### 2. Активировать виртуальное окружение

Windows (PowerShell):
```powershell
venv\Scripts\Activate.ps1
```

Windows (CMD):
```cmd
venv\Scripts\activate.bat
```

Linux / macOS:
```bash
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Применить миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Создать суперпользователя

```bash
python manage.py createsuperuser
```

Введите:
- **Имя пользователя**: например, `admin`
- **Email**: например, `admin@hospital.ru`
- **Пароль**: придумайте надёжный пароль

### 6. Запустить сервер разработки

```bash
python manage.py runserver
```

Откройте в браузере: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 📊 Модели данных

| Модель | Описание |
|--------|----------|
| `UserProfile` | Пациент (расширяет AbstractUser) |
| `Specialization` | Медицинская специализация |
| `Doctor` | Врач клиники |
| `Schedule` | Расписание врача |
| `Appointment` | Запись на приём |
| `MedicalRecord` | Медицинская запись после приёма |
| `DoctorReview` | Отзыв пациента о враче |

## 🔗 Связи между моделями

```
UserProfile ←── Appointment ──→ Doctor ←── Specialization
                    │               │
                    ↓               └──→ Schedule
             MedicalRecord
                                    ↑
UserProfile ←── DoctorReview ──→ Doctor
```

## 📝 Методы модели Doctor

- `get_avg_rating()` — возвращает средний рейтинг врача (из отзывов)
- `get_appointment_count()` — возвращает количество записей к врачу

## 🛠️ Технологии

- **Django 4.2** (LTS)
- **SQLite** (база данных для разработки)
- **Pillow** (работа с изображениями)

## 📚 Образовательные цели

Проект демонстрирует:
- `ForeignKey` — связь многие-к-одному
- `OneToOneField` — связь один-к-одному
- `AbstractUser` — расширение стандартной модели пользователя
- `choices` — ограниченный набор значений
- `validators` — валидация данных
- `related_name` — обратные связи
- `auto_now_add` — автоматическая дата
- Кастомные методы модели
- Настройка Django Admin
