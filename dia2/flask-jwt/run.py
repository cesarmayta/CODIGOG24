from flask import Flask,jsonify
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

app.run(debug=True)
