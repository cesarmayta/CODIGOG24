# paso 1
python -m venv venv

# paso 2
source venv/Scripts/activate

# paso 3
pip install -r requirements.txt

# paso 4 - creamos un proyecto con django
django-admin startproject peliculas

# paso 5 - creamos una app con django
cd peliculas
python manage.py startapp api

# para desplegar aplicación
python manage.py runserver

# para migrar modelo a base de datos
python manage.py makemigrations
python manage.py migrate

# para crear un super usuario
python manage.py createsuperuser