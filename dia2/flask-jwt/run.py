from flask import Flask,jsonify,request
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token
)

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'QWERTY123'
jwt = JWTManager(app)

@app.route('/publico',methods=['GET','POST','PUT','DELETE'])
def publico():
    context = {
        'message':'acceso publico'
    }
    return jsonify(context)

@app.route('/privado')
@jwt_required()
def privado():
    context = {
        'message':'acceso privado'
    }
    return jsonify(context)

@app.route('/login',methods=['POST'])
def login():
    usuario = request.json.get('usuario',None)
    password = request.json.get('password',None)

    if usuario == 'admin' and password == '123':
        payload = {
            'usuario':'cesar',
            'email':'cesarmayta@gmail.com',
            'id':1
        }
        token = create_access_token(payload)
        context = {
            'message':'bienvenido cesar',
            'content':token
        }
    else:
        context = {
            'message':'datos invalidos'
        }

    return jsonify(context)


app.run(debug=True)
