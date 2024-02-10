from flask_restful import Resource,Api
from flask import request

from .. import shop
from ..models import Producto

api = Api(shop)

class ProductoResource(Resource):

    def get(self):
        context = {
            'status':True,
            'message':'listado de productos'
        }

        return context

api.add_resource(ProductoResource,'/producto')