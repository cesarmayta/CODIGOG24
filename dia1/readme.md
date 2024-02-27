#creación de entorno virtual

python -m venv venv
source venv/Scripts/activate

#instalación de dependencias
pip install -r requirements.txt

#creación de proyecto y app
django-admin startproject ecommerce
cd ecommerce
python manage.py startapp web

#comandos para migraciones
python manage.py makemigrations
python manage.py migrate
