#para hacer migraciones
flask db init(solo se ejecuta una vez) si ya lo ejecutaste y tienes ya la carpeta migrations creada entonces no debes volver a ejecutarlo


flask db migrate -m "aqui pones un comentario"
flask db upgrade
