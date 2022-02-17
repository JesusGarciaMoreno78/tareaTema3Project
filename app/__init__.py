#Para poder usar Flask devemos incluirlo en el archivo requerimens para poder instalarlo

from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#pag 23 pps0303-Entrada de aula virtual
#Establecer la cadena de conexion
app = Flask(__name__)
app.secret_key="clave"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tareaTema3Projet'
#desactivamos la gestion de notificaciones de SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Instanciamos un objeto de la cxlase SQLAlchemy
db = SQLAlchemy(app)

#pag 25 pps0303-Entrada de aula virtual
#Instanciar un objeto de la classe Migrate
migrate = Migrate(app,db)

from .public import public
from .private import private

def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    return app