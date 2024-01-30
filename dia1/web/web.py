from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hola mundo web con flask</h1>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre','nn')
    return f'<center><b>hola {nombre}</b></center>'

@app.route('/suma')
def suma():
    n1 = request.args.get('n1','0')
    n2 = request.args.get('n2','0')
    resultado = int(n1) + int(n2)
    return f'<h1><center>LA SUMA DE {n1} + {n2} ES {resultado}</center></h1>'

@app.route('/<operacion>/<int:n1>/<int:n2>')
def calculadora(operacion='niguna',n1=0,n2=0):
    if operacion == 'suma':
        resultado = n1 + n2
    elif operacion == 'resta':
        resultado = n1 - n2
    elif operacion == 'multiplicacion':
        resultado = n1 * n2
    else:
        resultado = 'nn'

    return f'<h1> la {operacion} de {n1} y {n2} es {resultado}</h1>'

app.run(debug=True)