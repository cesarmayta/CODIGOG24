from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'asistencia'

mysql = MySQL(app)
print("conectado a la base de datos")

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)
