from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/db_todolist'
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.run(debug=True)