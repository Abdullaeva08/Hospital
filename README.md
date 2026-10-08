# 🏥 Hospital - Медицинская клиника

Образовательный Django проект для управления медицинской клиникой.

## 📋 Возможности

- ✅ Регистрация и авторизация пациентов
- ✅ Просмотр списка врачей и их специализаций
- ✅ Запись на приём к врачу
- ✅ Просмотр своих записей
- ✅ Оставление отзывов о врачах
- ✅ Загрузка фотографий для врачей и специализаций
- ✅ Административная панель

## 🛠️ Технологии

- **Backend**: Django 4.2.0
- **Frontend**: Bootstrap 5, Font Awesome
- **Database**: SQLite3
- **Python**: 3.14.5

## 📦 Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/your-username/Hospital.git
cd Hospital
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Применение миграций

```bash
python manage.py migrate
```

### 5. Создание суперпользователя

```bash
python manage.py createsuperuser
```

Или запустите скрипт:

```bash
python create_superuser.py
```

### 6. Загрузка тестовых данных (опционально)

```bash
python add_sample_data.py
```

### 7. Запуск сервера

```bash
python manage.py runserver
```

Откройте браузер: http://127.0.0.1:8000/

## 📸 Загрузка фотографий

Перейдите на страницу управления фотографиями:
http://127.0.0.1:8000/photos/

Здесь вы можете загрузить фото для:

- Врачей
- Специализаций
- Профиля пациента

## 🔐 Тестовые учетные данные

**Администратор:**

- Логин: `admin`
- Пароль: `admin123`

## 📁 Структура проекта

```
Hospital/
├── clinic/                  # Главное приложение
│   ├── models.py           # Модели БД
│   ├── views.py            # Представления
│   ├── views_upload.py     # Загрузка фото
│   ├── forms.py            # Формы
│   ├── admin.py            # Админ-панель
│   └── templates/          # HTML шаблоны
├── hospital_project/        # Настройки проекта
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                   # Загруженные файлы
├── static/                  # Статические файлы
├── manage.py
├── requirements.txt
└── README.md
```

## 🎓 Образовательный проект

Этот проект создан в образовательных целях для изучения Django Framework.

## 📝 Модели

- **UserProfile** - Профиль пациента
- **Specialization** - Медицинские специализации
- **Doctor** - Врачи клиники
- **Schedule** - Расписание работы врачей
- **Appointment** - Записи на приём
- **MedicalRecord** - Медицинские записи
- **DoctorReview** - Отзывы о врачах

## 🌐 Основные URL

- `/` - Главная страница
- `/register/` - Регистрация
- `/login/` - Вход
- `/doctors/` - Список врачей
- `/specializations/` - Специализации
- `/appointments/my/` - Мои записи
- `/photos/` - Управление фото
- `/admin/` - Админ-панель

## 📄 Лицензия

Образовательный проект. Свободное использование.

## 👨‍💻 Автор

Создано с помощью Kiro AI
