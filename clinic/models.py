"""
Модели данных для медицинской клиники.
Образовательный проект — Django models.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


# =====================
# 1. Профиль пользователя (пациент)
# =====================
class UserProfile(AbstractUser):
    """Расширенная модель пользователя — профиль пациента."""

    # Варианты групп крови
    BLOOD_GROUP_CHOICES = [
        ('O+', 'O (I) Rh+'),
        ('O-', 'O (I) Rh-'),
        ('A+', 'A (II) Rh+'),
        ('A-', 'A (II) Rh-'),
        ('B+', 'B (III) Rh+'),
        ('B-', 'B (III) Rh-'),
        ('AB+', 'AB (IV) Rh+'),
        ('AB-', 'AB (IV) Rh-'),
    ]

    birth_date = models.DateField(
        verbose_name='Дата рождения',
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name='Номер телефона',
        blank=True
    )
    address = models.TextField(
        verbose_name='Адрес',
        blank=True
    )
    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUP_CHOICES,
        verbose_name='Группа крови',
        blank=True
    )
    date_register = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='patients/',
        verbose_name='Фото профиля',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.username})'


# =====================
# 2. Специализация врача
# =====================
class Specialization(models.Model):
    """Медицинская специализация (кардиолог, хирург, терапевт и т.д.)."""

    name = models.CharField(
        max_length=100,
        verbose_name='Название специализации'
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    image = models.ImageField(
        upload_to='specializations/',
        verbose_name='Изображение',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


# =====================
# 3. Врач
# =====================
class Doctor(models.Model):
    """Модель врача клиники."""

    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )
    patronymic = models.CharField(
        max_length=100,
        verbose_name='Отчество',
        blank=True
    )
    photo = models.ImageField(
        upload_to='doctors/',
        verbose_name='Фото',
        null=True,
        blank=True
    )
    experience_years = models.IntegerField(
        verbose_name='Опыт (лет)',
        default=0,
        validators=[MinValueValidator(0)]
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена приёма (руб.)'
    )
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.PROTECT,
        related_name='doctors',
        verbose_name='Специализация'
    )

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'.strip()

    def get_avg_rating(self):
        """Возвращает средний рейтинг врача по отзывам."""
        reviews = self.reviews.all()
        if not reviews.exists():
            return 0
        total = sum(review.stars for review in reviews)
        return round(total / reviews.count(), 1)

    def get_appointment_count(self):
        """Возвращает количество записей к данному врачу."""
        return self.appointments.count()


# =====================
# 4. Расписание врача
# =====================
class Schedule(models.Model):
    """Расписание работы врача по дням недели."""

    # Дни недели
    DAY_CHOICES = [
        ('MON', 'Понедельник'),
        ('TUE', 'Вторник'),
        ('WED', 'Среда'),
        ('THU', 'Четверг'),
        ('FRI', 'Пятница'),
        ('SAT', 'Суббота'),
        ('SUN', 'Воскресенье'),
    ]

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='schedules',
        verbose_name='Врач'
    )
    day_of_week = models.CharField(
        max_length=3,
        choices=DAY_CHOICES,
        verbose_name='День недели'
    )
    start_time = models.TimeField(
        verbose_name='Время начала'
    )
    end_time = models.TimeField(
        verbose_name='Время окончания'
    )

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        # Врач не может иметь два расписания на один день
        unique_together = ('doctor', 'day_of_week')

    def __str__(self):
        return f'{self.doctor} — {self.get_day_of_week_display()} ({self.start_time}–{self.end_time})'


# =====================
# 5. Запись на приём
# =====================
class Appointment(models.Model):
    """Запись пациента к врачу."""

    # Статусы записи
    STATUS_CHOICES = [
        ('pending', 'Ожидает подтверждения'),
        ('confirmed', 'Подтверждена'),
        ('cancelled', 'Отменена'),
        ('completed', 'Завершена'),
    ]

    patient = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='Пациент'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments',
        verbose_name='Врач'
    )
    date_time = models.DateTimeField(
        verbose_name='Дата и время приёма'
    )
    complaint = models.TextField(
        verbose_name='Жалоба'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Запись на приём'
        verbose_name_plural = 'Записи на приём'
        ordering = ['-date_time']

    def __str__(self):
        return f'{self.patient} → {self.doctor} [{self.date_time.strftime("%d.%m.%Y %H:%M")}]'


# =====================
# 6. Медицинская запись
# =====================
class MedicalRecord(models.Model):
    """Медицинская запись после приёма врача."""

    # OneToOne: одна запись на приём — одна медкарта
    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE,
        related_name='medical_record',
        verbose_name='Запись на приём'
    )
    diagnosis = models.TextField(
        verbose_name='Диагноз'
    )
    prescription = models.TextField(
        verbose_name='Назначения'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Медицинская запись'
        verbose_name_plural = 'Медицинские записи'

    def __str__(self):
        return f'Мед. запись: {self.appointment}'


# =====================
# 7. Отзыв на врача
# =====================
class DoctorReview(models.Model):
    """Отзыв пациента о враче с оценкой от 1 до 5."""

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Врач'
    )
    patient = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Пациент'
    )
    stars = models.IntegerField(
        verbose_name='Оценка',
        validators=[
            MinValueValidator(1, message='Минимальная оценка — 1'),
            MaxValueValidator(5, message='Максимальная оценка — 5')
        ]
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата отзыва'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        # Пациент может оставить только один отзыв на врача
        unique_together = ('doctor', 'patient')

    def __str__(self):
        return f'{self.patient} → {self.doctor}: {self.stars}★'
