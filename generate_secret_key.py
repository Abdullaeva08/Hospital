"""
Жаңы SECRET_KEY генерациялоо скрипти
"""
from django.core.management.utils import get_random_secret_key

# Жаңы купуя ачкычты генерациялоо
new_secret_key = get_random_secret_key()

print("=" * 70)
print("🔐 ЖАҢЫ SECRET_KEY ГЕНЕРАЦИЯЛАНДЫ:")
print("=" * 70)
print(new_secret_key)
print("=" * 70)
print("\n📋 Муну көчүрүп алып, settings.py файлына коюңуз:")
print(f"\nSECRET_KEY = '{new_secret_key}'")
print("\n✅ Бул купуя ачкыч эч кимге берилбейт!")
print("❌ GitHub'га жүктөбөңүз!")
print("=" * 70)
