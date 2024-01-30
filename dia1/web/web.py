from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hola mundo web con flask</h1>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre','nn')
    return f'<center><b>hola {nombre}</b></center>'

app.run(debug=True)