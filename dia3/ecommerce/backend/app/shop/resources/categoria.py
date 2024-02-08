from flask_restful import Resource,Api
from flask import request

from .. import shop
from ..models import Categoria

api = Api(shop)

class CategoriaResource(Resource):
    
    def get(self):
        context = {
            'status':True,
            'message':'listado de categorias'
        }
        
        return context
    
api.add_resource(CategoriaResource,'/categoria')