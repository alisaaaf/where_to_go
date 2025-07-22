
# Where to Go

**Where to Go** is a website showcasing interesting travel spots.  
The project demonstrates working with Django, the admin interface, APIs, and front-end visualization based on layout templates.

## - Local Installation

1. Clone the repository:

```bash
git clone https://github.com/alisaaaf/where_to_go.git
cd where_to_go
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add the following variables:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Create an admin user:

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

## - Project Features

- Upload travel spots data via JSON files
- Django Admin with convenient object management
- Interactive map with location markers

## - Deployment

The project is deployed for demo purposes on the free hosting service [PythonAnywhere](https://www.pythonanywhere.com/).

