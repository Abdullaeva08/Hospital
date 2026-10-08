"""Представления для медицинской клиники"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import UserProfile, Specialization, Doctor, Appointment, MedicalRecord, DoctorReview
from .forms import UserRegistrationForm, UserLoginForm, ProfileEditForm, AppointmentForm, ReviewForm

def index(request):
    specializations = Specialization.objects.all()[:6]
    doctors_count = Doctor.objects.count()
    context = {'specializations': specializations, 'doctors_count': doctors_count}
    return render(request, 'clinic/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('clinic:index')
    else:
        form = UserRegistrationForm()
    return render(request, 'clinic/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {user.first_name}!')
                return redirect('clinic:index')
    else:
        form = UserLoginForm()
    return render(request, 'clinic/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы')
    return redirect('clinic:index')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлён!')
            return redirect('clinic:profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'clinic/profile.html', {'form': form})

def doctors_list(request):
    doctors = Doctor.objects.select_related('specialization').all()
    specialization_id = request.GET.get('specialization')
    if specialization_id:
        doctors = doctors.filter(specialization_id=specialization_id)
    search = request.GET.get('search')
    if search:
        doctors = doctors.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
    specializations = Specialization.objects.all()
    return render(request, 'clinic/doctors_list.html', {'doctors': doctors, 'specializations': specializations})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor.objects.select_related('specialization').prefetch_related('schedules', 'reviews__patient'), id=doctor_id)
    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.doctor = doctor
            review.patient = request.user
            try:
                review.save()
                messages.success(request, 'Спасибо за отзыв!')
                return redirect('clinic:doctor_detail', doctor_id=doctor.id)
            except:
                messages.error(request, 'Вы уже оставили отзыв')
    else:
        form = ReviewForm()
    user_has_review = request.user.is_authenticated and DoctorReview.objects.filter(doctor=doctor, patient=request.user).exists()
    context = {'doctor': doctor, 'schedules': doctor.schedules.all(), 'reviews': doctor.reviews.all().order_by('-created_date'), 'review_form': form, 'user_has_review': user_has_review, 'avg_rating': doctor.get_avg_rating(), 'appointment_count': doctor.get_appointment_count()}
    return render(request, 'clinic/doctor_detail.html', context)

@login_required
def book_appointment(request, doctor_id=None):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.status = 'pending'
            appointment.save()
            messages.success(request, 'Запись создана!')
            return redirect('clinic:my_appointments')
    else:
        initial = {'doctor': doctor_id} if doctor_id else {}
        form = AppointmentForm(initial=initial)
    return render(request, 'clinic/book_appointment.html', {'form': form})

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user).select_related('doctor__specialization').order_by('-date_time')
    for apt in appointments:
        try:
            apt.record = apt.medical_record
        except:
            apt.record = None
    return render(request, 'clinic/my_appointments.html', {'appointments': appointments})

def specializations_list(request):
    return render(request, 'clinic/specializations_list.html', {'specializations': Specialization.objects.all()})
