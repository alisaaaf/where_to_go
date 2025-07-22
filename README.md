# Where to go

**Where to go** — это сайт с подборкой интересных мест для путешествий.  
Проект демонстрирует работу с Django, админкой, API и front-end визуализацией на основе верстки.


##  - Установка проекта локально

1. Клонируйте репозиторий:

```bash
git https://github.com/alisaaaf/where_to_go.git
cd where_to_go
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` и укажите в нем переменные:

```bash
SECRET_KEY=ваш_секретный_ключ
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

4. Выполните миграции:

```bash
python manage.py migrate
```

5. Создайте администратора:

```bash
python manage.py createsuperuser
```

6. Запустите сервер:

```bash
python manage.py runserver
```

## - Особенности проекта

- Загрузка данных о местах через JSON-файлы
- Django Admin с удобным управлением объектами
- Интерактивная карта с отметками мест

## - Деплой

Проект загружен на бесплатном хостинге [PythonAnywhere](https://www.pythonanywhere.com/).


