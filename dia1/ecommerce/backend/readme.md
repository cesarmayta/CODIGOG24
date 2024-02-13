#para hacer migraciones
flask db init(solo se ejecuta una vez)

flask db migrate -m "categorias"
flask db upgrade

###
CREAR dentro del archivo models.py 
el modelo para la tabla marca con los mismos campos de categoria
y realizar la migración a la base de datos
10 min

NOTA: debe importar el modelo en el resource de marca