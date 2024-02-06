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
                   CREATE TABLE IF NOT EXITS tarea(
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

if __name__ == '__main__':
    app.run(debug=True)