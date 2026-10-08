"""
Представления для загрузки фотографий без админки.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Doctor, Specialization, UserProfile
from .forms import DoctorPhotoForm, SpecializationPhotoForm


@login_required
def upload_doctor_photo(request, doctor_id):
    """Загрузка фото для врача."""
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    if request.method == 'POST':
        form = DoctorPhotoForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, f'Фото для врача {doctor} успешно загружено!')
            return redirect('clinic:doctors_list')
    else:
        form = DoctorPhotoForm(instance=doctor)
    
    return render(request, 'clinic/upload_doctor_photo.html', {
        'form': form,
        'doctor': doctor
    })


@login_required
def upload_specialization_photo(request, spec_id):
    """Загрузка фото для специализации."""
    specialization = get_object_or_404(Specialization, id=spec_id)
    
    if request.method == 'POST':
        form = SpecializationPhotoForm(request.POST, request.FILES, instance=specialization)
        if form.is_valid():
            form.save()
            messages.success(request, f'Фото для специализации {specialization} успешно загружено!')
            return redirect('clinic:specializations_list')
    else:
        form = SpecializationPhotoForm(instance=specialization)
    
    return render(request, 'clinic/upload_specialization_photo.html', {
        'form': form,
        'specialization': specialization
    })


@login_required
def manage_photos(request):
    """Страница управления всеми фотографиями."""
    doctors = Doctor.objects.all()
    specializations = Specialization.objects.all()
    
    return render(request, 'clinic/manage_photos.html', {
        'doctors': doctors,
        'specializations': specializations
    })
