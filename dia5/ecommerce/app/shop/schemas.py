from utils import ma

from .models import (
    Producto
)

class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Producto