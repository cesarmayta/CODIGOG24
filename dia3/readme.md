# para instalar django
python -m venv venv
source venv/Scripts/activate
pip install django==4.2

# comandos para crear y desplegar un proyecto con django
django-admin startproject peliculas
cd peliculas
python manage.py runserver

# comando para crear un app
python manage.py startapp web