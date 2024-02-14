from flask_restful import Resource,Api
from flask import request
from .. import auth
from ..models import Usuario

api = Api(auth)

class UsuarioResource(Resource):

    def get(self):
        context = {
            'status':True,
            'message':'listado de usuarios'
        }
        return context

api.add_resource(UsuarioResource,'/user')