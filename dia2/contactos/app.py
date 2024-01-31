import requests
from flask import Flask,request,render_template

app = Flask(__name__)

url = 'https://randomuser.me/api/?results=3&nat=es'

@app.route('/')
def index():
    lista_contactos = requests.get(url).json()
    print(lista_contactos)
    
    return render_template('index.html',contactos=lista_contactos['results'])

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')


if __name__ == '__main__':
    app.run(debug=True)