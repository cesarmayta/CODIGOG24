from flask_restful import Resource,Api
from flask import request

from .. import shop
from ..models import Marca

api = Api(shop)

class MarcaResource(Resource):
    
    def get(self):
        context = {
            'status':True,
            'message':'listado de marcas'
        }
        
        return context
    
api.add_resource(MarcaResource,'/marca')