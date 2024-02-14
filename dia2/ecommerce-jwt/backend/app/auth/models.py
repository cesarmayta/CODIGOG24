from utils import db

class Usuario(db.Model):
    __tablename__ = 'tbl_usuario'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(200),nullable=False,unique=True)
    password = db.Column(db.Text,nullable=False)
    is_admin = db.Column(db.Boolean,default=False)