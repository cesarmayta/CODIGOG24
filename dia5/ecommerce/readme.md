#creación de variables de entorno para flask
export FLASK_APP=run.py
export FLASK_DEBUG=1

#para migraciones
flask db init
flask db migrate -m "comentario"
flask db upgrade