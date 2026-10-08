"""
Скрипт для загрузки демо-фотографий врачей
"""
import os
import django
import requests
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospital_project.settings')
django.setup()

from clinic.models import Doctor, Specialization
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

# Создаём папку для фото
MEDIA_ROOT = Path('media')
MEDIA_ROOT.mkdir(exist_ok=True)
(MEDIA_ROOT / 'doctors').mkdir(exist_ok=True)
(MEDIA_ROOT / 'specializations').mkdir(exist_ok=True)

# URL аватарок (используем placeholder сервис)
def get_doctor_photo_url(name):
    """Генерируем URL для аватара врача"""
    # Используем UI Avatars для генерации аватаров
    return f"https://ui-avatars.com/api/?name={name}&size=400&background=667eea&color=fff&bold=true"

# Фото для специализаций
specialization_photos = {
    'Кардиология': 'https://images.unsplash.com/photo-1628348068343-c6a848d2b6dd?w=400',
    'Терапия': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400',
    'Хирургия': 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?w=400',
    'Неврология': 'https://images.unsplash.com/photo-1559757175-5700dde675bc?w=400',
    'Педиатрия': 'https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?w=400',
    'Стоматология': 'https://images.unsplash.com/photo-1606811841689-23dfddce3e95?w=400',
}

print('📸 Загрузка фотографий для врачей...')

doctors = Doctor.objects.all()
for doctor in doctors:
    if not doctor.photo:
        try:
            name = f"{doctor.first_name}+{doctor.last_name}"
            url = get_doctor_photo_url(name)
            
            response = requests.get(url)
            if response.status_code == 200:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()
                
                filename = f"{doctor.last_name}_{doctor.first_name}.jpg"
                doctor.photo.save(filename, File(img_temp), save=True)
                print(f'✅ Фото добавлено для: {doctor}')
        except Exception as e:
            print(f'❌ Ошибка при загрузке фото для {doctor}: {e}')

print('\n📸 Загрузка изображений для специализаций...')

for spec_name, photo_url in specialization_photos.items():
    try:
        spec = Specialization.objects.get(name=spec_name)
        if not spec.image:
            response = requests.get(photo_url)
            if response.status_code == 200:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()
                
                filename = f"{spec_name}.jpg"
                spec.image.save(filename, File(img_temp), save=True)
                print(f'✅ Изображение добавлено для: {spec_name}')
    except Specialization.DoesNotExist:
        print(f'⚠️  Специализация "{spec_name}" не найдена')
    except Exception as e:
        print(f'❌ Ошибка при загрузке изображения для {spec_name}: {e}')

print('\n🎉 Готово! Фотографии загружены.')
print('💡 Совет: Вы можете загрузить свои фото через админ-панель:')
print('   http://127.0.0.1:8000/admin/')
