from flask_restful import Resource,Api
from flask import request
from .. import auth
from ..models import Usuario

from werkzeug.security import(
    generate_password_hash,
    check_password_hash
)

api = Api(auth)

class UsuarioResource(Resource):

    def post(self):
        data = request.get_json()
        password = data['password']
        password_hash = generate_password_hash(password)
        usuario = Usuario()
        usuario.email = data['email']
        usuario.password = password_hash
        usuario.save()

        context = {
            'status':True,
            'message':'usuario registrado'
        }

        return context

        

    def get(self):
        context = {
            'status':True,
            'message':'listado de usuarios'
        }
        return context

api.add_resource(UsuarioResource,'/user')