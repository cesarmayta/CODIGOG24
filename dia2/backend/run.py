from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.app_context().push()

#mysql://usuario:password@host/basedatos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/db_todolist'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

### creando tabla con el ORM ###
class Tarea(db.Model):
    id = db.Column(db.Integer,primary_key=True) # id INT NOT NUL PRIMARY KEY
    descripcion = db.Column(db.String(200),nullable=False) #descripcion VARCHAR(200) NOT NULL
    estado = db.Column(db.String(100),nullable=False)
    
    def __init__(self,descripcion,estado):
        self.descripcion = descripcion
        self.estado = estado

# esquemas#
ma = Marshmallow(app)
class TareaSchema(ma.Schema):
    class Meta:
        fields = ('id','descripcion','estado')

db.create_all()
print('se creo la tabla tarea en la base de datos')


@app.route('/tarea',methods=['POST'])
def set_tarea():
    descripcion = request.json['descripcion']
    estado = request.json['estado']
    
    #insert into tarea...
    nueva_tarea = Tarea(descripcion,estado)
    db.session.add(nueva_tarea)
    db.session.commit()
    
    data_schema = TareaSchema()
    
    context = {
        'status':True,
        'message':'registro exitoso',
        'content': data_schema.dump(nueva_tarea)
    }

    return jsonify(context)

@app.route('/tarea')
def get_tarea():
    data = Tarea.query.all() #select id,descripcion,estado from tarea
    print(data)
    data_schema = TareaSchema(many=True)
    
    context = {
        'status':True,
        'content': data_schema.dump(data)
    }
    
    return jsonify(context)
    

app.run(debug=True)