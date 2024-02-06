from flask import Flask,request,jsonify
from flask_mysqldb import MySQL 


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'api_rest'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tarea(
                       id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                       descripcion VARCHAR(255) NOT NULL,
                       estado VARCHAR(100) DEFAULT 'pendiente'
                   );
                   """)
    mysql.connection.commit()
    cursor.close()
    print('TABLA CREADA!!!')
    
    context = {
        'status':True,
        'message':'Mi primer api rest con flask'
    }
    return jsonify(context)

@app.route('/tarea')
def get_tarea():
    cursor = mysql.connection.cursor()
    cursor.execute('select id,descripcion,estado from tarea')
    data = cursor.fetchall()
    print(data)
    cursor.close()
    
    context = {
        'status':True,
        'content':data
    }
    
    return jsonify(context)

@app.route('/tarea',methods=['POST'])
def set_tarea():
    descripcion = request.json['descripcion']
    
    cursor =  mysql.connection.cursor()
    cursor.execute(f"insert into tarea(descripcion) values('{descripcion}');")
    #cursor.execute(f"CALL sp_insertar_tarea('{descripcion}')")
    mysql.connection.commit()
    cursor.close()
    
    cursor_data = mysql.connection.cursor()
    cursor_data.execute('select id,descripcion,estado from tarea order by id desc limit 1')
    data = cursor_data.fetchall()
    cursor_data.close()
    
    context = {
        'status':True,
        'message':'registro exitoso',
        'content':data[0]
    }
    
    return jsonify(context)

@app.route('/tarea/<id>')
def get_tarea_id(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f'select id,descripcion,estado from tarea where id={id}')
    data = cursor.fetchall()
    cursor.close()
    
    context = {
        'status':True,
        'content':data[0]
    }
    
    return jsonify(context)

@app.route('/tarea/<id>',methods=['PUT'])
def update_tarea(id):
    descripcion = request.json['descripcion']
    estado = request.json['estado']
    
    cursor = mysql.connection.cursor()
    cursor.execute(f"update tarea set descripcion='{descripcion}',estado='{estado}' where id={id}")
    mysql.connection.commit()
    cursor.close()
    
    context = {
        'status':True,
        'content':'',
        'message':'registro actualizado'
    }
    
    return jsonify(context)
    


if __name__ == '__main__':
    app.run(debug=True)