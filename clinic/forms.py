"""Формы для медицинской клиники"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile, Appointment, DoctorReview, Doctor, Specialization

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    phone_number = forms.CharField(label='Номер телефона', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+7 (999) 123-45-67'}))
    address = forms.CharField(label='Адрес', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    blood_group = forms.ChoiceField(label='Группа крови', choices=UserProfile.BLOOD_GROUP_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'first_name', 'last_name', 'birth_date', 'phone_number', 'address', 'blood_group', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'first_name', 'last_name', 'email', 'birth_date', 'phone_number', 'address', 'blood_group']
        widgets = {
            'photo': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
        }

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date_time', 'complaint']
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'date_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'complaint': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Опишите ваши жалобы...'}),
        }
        labels = {'doctor': 'Врач', 'date_time': 'Дата и время приёма', 'complaint': 'Жалобы'}

class ReviewForm(forms.ModelForm):
    class Meta:
        model = DoctorReview
        fields = ['stars', 'comment']
        widgets = {
            'stars': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ваш отзыв о враче...'}),
        }
        labels = {'stars': 'Оценка (1-5)', 'comment': 'Комментарий'}


# =====================
# Формы для загрузки фото
# =====================

class DoctorPhotoForm(forms.ModelForm):
    """Форма загрузки фото врача."""
    
    class Meta:
        model = Doctor
        fields = ['photo']
        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }


class SpecializationPhotoForm(forms.ModelForm):
    """Форма загрузки фото специализации."""
    
    class Meta:
        model = Specialization
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }
