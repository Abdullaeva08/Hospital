# 📤 GitHub'га жүктөө көрсөтмөсү

## Толук кыргызча нускама

### 1️⃣ GitHub'та репозиторий түзүңүз

1. **GitHub сайтына кириңиз**: https://github.com
2. **Жашыл "New"** баскычын басыңыз (же "+" белгиси)
3. **Repository name** (Репозиторийдин аты): `Hospital` деп жазыңыз
4. **Description** (Сүрөттөмө): `Медициналык клиника - Django проекти`
5. **Public** (Ачык) же **Private** (Жеке) тандаңыз
6. ❌ **МААНИЛҮҮ**: "Initialize this repository with a README" деген жерге галочка **КОЮП КАЛБАҢЫЗ**
7. Ачык көк түстөгү **"Create repository"** баскычын басыңыз

### 2️⃣ Репозиторийдин URL дарегин көчүрүп алыңыз

GitHub сизге жаңы баракча ачып, анда URL дарегин көрсөтөт:
```
https://github.com/sizdin-atynyz/Hospital.git
```

**Бул URL дарегин көчүрүп алыңыз!** (Ctrl+C басыңыз) ☝️

### 3️⃣ Өзүңүздүн компьютериңизден GitHub'га жүктөңүз

**PowerShell** же **Terminal** ачып, төмөнкү командаларды жазыңыз:

#### Биринчи - Hospital папкасына кириңиз:
```bash
cd C:\Users\user\Desktop\Hospital
```

#### Экинчи - GitHub репозиторийин улаңыз:
```bash
git remote add origin https://github.com/SIZDIN-ATYNYZ/Hospital.git
```

⚠️ **SIZDIN-ATYNYZ** ордуна өзүңүздүн GitHub логиниңизди жазыңыз!

#### Үчүнчү - Негизги тармакты атаңыз:
```bash
git branch -M main
```

#### Төртүнчү - Баарын GitHub'га жиберүү:
```bash
git push -u origin main
```

### 4️⃣ Логин жана парол киргизиңиз

GitHub логин жана парол сурайт:
- **Username (Колдонуучу аты)**: Сиздин GitHub логиниңиз
- **Password (Парол)**: ❌ Жөнөкөй паролду **ЭМЕС**, **Personal Access Token** колдонуңуз!

---

## 🔑 Personal Access Token (Токен) алуу

Эгерде парол иштебесе, токен алышыңыз керек:

### Токен алуу жолу:

1. **GitHub'та Settings (Тууралоолор) ачыңыз**:
   - Оң жак жогорку бурчтагы сиздин сүрөткөөңүздү басыңыз
   - **Settings** тандаңыз

2. **Developer settings ачыңыз**:
   - Сол жактагы тизмеден эң аягында **Developer settings** басыңыз

3. **Personal access tokens ачыңыз**:
   - **Personal access tokens** → **Tokens (classic)** басыңыз

4. **Жаңы токен түзүңүз**:
   - **"Generate new token"** басыңыз
   - **"Generate new token (classic)"** тандаңыз

5. **Токенди толтуруңуз**:
   - **Note** (Аты): `Hospital Project` деп жазыңыз
   - **Expiration** (Мөөнөтү): `90 days` же `No expiration` (мөөнөтсүз)
   - **Галочка коюңуз**: ✅ **repo** (баарын тандайт)

6. **Жашыл "Generate token" басыңыз**

7. **МААНИЛҮҮ**: Токенди көчүрүп алыңыз! Бул бир жолу гана көрүнөт!

8. **git push** командасын киргизгенде:
   - **Username**: GitHub логиниңиз
   - **Password**: Токенди (көчүргөн tokenди) коюңуз

---

## ✅ Даяр! Сиздин проектиңиз GitHub'та!

Эми браузерде репозиторийди ачып көрүңүз:
```
https://github.com/SIZDIN-ATYNYZ/Hospital
```

🎉 **Куттуктайбыз! Проектиңиз интернетте!** 🎉

---

## 🔄 Кийинчерээк өзгөртүүлөрдү жүктөө

Эгер кодду өзгөртсөңүз жана GitHub'га кайрадан жүктөгүңүз келсе:

### 1. Баардык өзгөрүүлөрдү кошуңуз:
```bash
git add .
```

### 2. Коммит жасаңыз (сүрөттөмө менен):
```bash
git commit -m "Жаңы функция кошулду"
```

### 3. GitHub'га жүктөңүз:
```bash
git push
```

### Мисалдар:

**Дизайн өзгөрткөндө:**
```bash
git add .
git commit -m "Башкы беттин дизайны өзгөртүлдү"
git push
```

**Жаңы функция кошкондо:**
```bash
git add .
git commit -m "Врачтар үчүн фото жүктөө мүмкүнчүлүгү кошулду"
git push
```

**Ката оңдогондо:**
```bash
git add .
git commit -m "Логин формасындагы ката оңдолду"
git push
```

---

## 📚 Пайдалуу Git командалары

### Статусту текшерүү (кандай файлдар өзгөртүлгөн):
```bash
git status
```

### Тарыхты көрүү (өткөн коммиттерди):
```bash
git log
```

### GitHub дарегин көрүү:
```bash
git remote -v
```

### GitHub дарегин өзгөртүү:
```bash
git remote set-url origin https://github.com/ЖАНЫ-ДАРЕК/Hospital.git
```

---

## ❓ Көп кездешүүчү маселелер жана чечимдери

### 1. "remote origin already exists" катасы

Буга жолуксаңыз, мындай кылыңыз:
```bash
git remote remove origin
git remote add origin https://github.com/SIZDIN-ATYNYZ/Hospital.git
git push -u origin main
```

### 2. "failed to push some refs" катасы

```bash
git pull origin main --rebase
git push -u origin main
```

### 3. "Authentication failed" - Логин туура эмес

Personal Access Token колдонуңуз (жогорудагы инструкцияны караңыз)

### 4. "Permission denied" - Уруксат жок

GitHub'та репозиторий туура түзүлгөнүн текшериңиз жана токенде **repo** укугу барын текшериңиз.

---

## 🎯 GitHub'та болгондон кийин эмне кыласыз?

Эми сиз:

- ✅ **Проектти башкалар менен бөлүшө аласыз** - жөн гана URL жиберип коюңуз
- ✅ **Портфолиого кошо аласыз** - иш издегенде көрсөтүүгө болот
- ✅ **Башка компьютерден иштей аласыз** - `git clone` менен жүктөп алып
- ✅ **Код үзүндүлөрүн көрсөтө аласыз** - мугалимге же досторго
- ✅ **Тарыхты сактайсыз** - ар бир өзгөртүү сакталат
- ✅ **Командада иштей аласыз** - башкалар да коштоп иштеши мүмкүн

---

## 📥 Башка компьютерден жүктөп алуу

Эгер башка компьютерден же ноутбуктан иштегиңиз келсе:

```bash
git clone https://github.com/SIZDIN-ATYNYZ/Hospital.git
cd Hospital
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 💡 Кеңештер

1. **Көп коммит кылыңыз** - ар бир чоң өзгөртүүдөн кийин
2. **Түшүнүктүү сүрөттөмө жазыңыз** - "эмне өзгөртүлдү" деп
3. **Купуя файлдарды жүктөбөңүз** - `.gitignore` алардын алдын алат
4. **Күн сайын push кылыңыз** - сактык үчүн

---

## 🎓 Видео көрсөтмөлөр (орусча):

YouTube'та издеңиз:
- "Git для начинающих"
- "Как загрузить проект на GitHub"
- "GitHub tutorial русский"

---

## 🆘 Жардам керек болсо:

1. GitHub документация: https://docs.github.com
2. Git документация (орусча): https://git-scm.com/book/ru/v2
3. Stack Overflow: https://stackoverflow.com

---

**Ийгилик! Проектиңиз ийгиликтүү GitHub'ка жүктөлсүн!** 🚀

**Суроолоруңуз болсо, суранып коюңуз!** 💬
