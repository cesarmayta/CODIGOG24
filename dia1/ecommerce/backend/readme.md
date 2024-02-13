#para hacer migraciones
flask db init(solo se ejecuta una vez)

flask db migrate -m "categorias"
flask db upgrade
