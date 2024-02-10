from utils import db

class Producto(db.Model):
    __tablename__ = 'producto'

    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(200),nullable=False)
    precio = db.Column(db.Double,default=0)
    imagen = db.Column(db.String(255))

    def __init__(self,nombre,precio,imagen):
        self.nombre = nombre
        self.precio = precio
        self.imagen = imagen
        