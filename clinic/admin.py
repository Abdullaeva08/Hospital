"""
Админ-панель для медицинской клиники.
Настройка отображения всех моделей.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    UserProfile, Specialization, Doctor,
    Schedule, Appointment, MedicalRecord, DoctorReview
)


# =====================
# Inline-классы (вложенные формы)
# =====================

class ScheduleInline(admin.TabularInline):
    """Расписание врача — показывается прямо на странице врача."""
    model = Schedule
    extra = 1  # Количество пустых форм по умолчанию
    fields = ('day_of_week', 'start_time', 'end_time')


class MedicalRecordInline(admin.StackedInline):
    """Медицинская запись — показывается на странице записи на приём."""
    model = MedicalRecord
    extra = 0
    can_delete = False


# =====================
# Регистрация модели UserProfile
# =====================
@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    """Админ-панель для пациентов."""

    # Дополнительные поля в списке
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'blood_group', 'is_staff')
    list_filter = ('is_staff', 'is_active', 'blood_group')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')

    # Добавляем наши поля в форму редактирования
    fieldsets = UserAdmin.fieldsets + (
        ('Профиль пациента', {
            'fields': ('birth_date', 'phone_number', 'address', 'blood_group')
        }),
    )

    # Поля при создании нового пользователя
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Профиль пациента', {
            'fields': ('first_name', 'last_name', 'email', 'birth_date', 'phone_number', 'address', 'blood_group')
        }),
    )


# =====================
# Регистрация модели Specialization
# =====================
@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """Админ-панель для специализаций."""

    list_display = ('name', 'description')
    search_fields = ('name',)


# =====================
# Регистрация модели Doctor
# =====================
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Админ-панель для врачей."""

    list_display = ('last_name', 'first_name', 'patronymic', 'specialization', 'experience_years', 'price', 'get_avg_rating', 'get_appointment_count')
    list_filter = ('specialization', 'experience_years')
    search_fields = ('first_name', 'last_name', 'patronymic')

    # Добавляем расписание прямо на странице врача
    inlines = [ScheduleInline]

    # Методы как колонки
    @admin.display(description='Средний рейтинг')
    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    @admin.display(description='Кол-во записей')
    def get_appointment_count(self, obj):
        return obj.get_appointment_count()


# =====================
# Регистрация модели Schedule
# =====================
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Админ-панель для расписания."""

    list_display = ('doctor', 'day_of_week', 'start_time', 'end_time')
    list_filter = ('day_of_week', 'doctor')
    search_fields = ('doctor__last_name', 'doctor__first_name')


# =====================
# Регистрация модели Appointment
# =====================
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """Админ-панель для записей на приём."""

    list_display = ('patient', 'doctor', 'date_time', 'status', 'created_date')
    list_filter = ('status', 'doctor', 'date_time')
    search_fields = ('patient__username', 'patient__first_name', 'doctor__last_name')
    date_hierarchy = 'date_time'

    # Медицинская запись прямо на странице приёма
    inlines = [MedicalRecordInline]

    # Быстрое изменение статуса
    list_editable = ('status',)
    actions = ['confirm_appointments', 'cancel_appointments', 'complete_appointments']

    @admin.action(description='Подтвердить выбранные записи')
    def confirm_appointments(self, request, queryset):
        queryset.update(status='confirmed')

    @admin.action(description='Отменить выбранные записи')
    def cancel_appointments(self, request, queryset):
        queryset.update(status='cancelled')

    @admin.action(description='Завершить выбранные записи')
    def complete_appointments(self, request, queryset):
        queryset.update(status='completed')


# =====================
# Регистрация модели MedicalRecord
# =====================
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    """Админ-панель для медицинских записей."""

    list_display = ('appointment', 'created_date')
    search_fields = ('appointment__patient__username', 'diagnosis')
    date_hierarchy = 'created_date'


# =====================
# Регистрация модели DoctorReview
# =====================
@admin.register(DoctorReview)
class DoctorReviewAdmin(admin.ModelAdmin):
    """Админ-панель для отзывов."""

    list_display = ('doctor', 'patient', 'stars', 'created_date')
    list_filter = ('stars', 'doctor')
    search_fields = ('doctor__last_name', 'patient__username')
