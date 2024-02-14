from flask import Flask,jsonify,request
from flask_jwt_extended import (
    JWTManager,jwt_required
)

app = Flask(__name__)

############## CONFIGURACION DE JWT ###########
app.config['JWT_SECRET_KEY'] = 'QWERTY1230'
jwt = JWTManager(app)
##############################################

@app.route('/publico')
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
