"""URL маршруты"""
from django.urls import path
from . import views, views_upload

app_name = 'clinic'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('appointments/book/', views.book_appointment, name='book_appointment'),
    path('appointments/book/<int:doctor_id>/', views.book_appointment, name='book_appointment_doctor'),
    path('appointments/my/', views.my_appointments, name='my_appointments'),
    path('specializations/', views.specializations_list, name='specializations_list'),
    
    # Загрузка фото
    path('photos/', views_upload.manage_photos, name='manage_photos'),
    path('photos/doctor/<int:doctor_id>/', views_upload.upload_doctor_photo, name='upload_doctor_photo'),
    path('photos/specialization/<int:spec_id>/', views_upload.upload_specialization_photo, name='upload_specialization_photo'),
]
