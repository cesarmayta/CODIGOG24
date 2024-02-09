from flask_restful import Resource,Api
from flask import request

from .. import shop
from ..models import Marca
from ..schemas import MarcaSchema

api = Api(shop)

class MarcaResource(Resource):
    
    def post(self):
        data = request.get_json()
        nombre = data['nombre']
        
        marca = Marca(nombre)
        marca.save()
        
        data_schema = MarcaSchema()
        
        context = {
            'status':True,
            'message':'Nuevo registro creado',
            'content':data_schema.dump(marca)
        }    
        
        return context
    
    def get(self):
        data = Marca.get_all()
        data_schema = MarcaSchema(many=True)
        
        context = {
            'status':True,
            'message':'listado de marcas',
            'content':data_schema.dump(data)
        }
        
        return context
    
api.add_resource(MarcaResource,'/marca')