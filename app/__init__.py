#Para poder usar Flask devemos incluirlo en el archivo requerimens para poder instalarlo
from flask import Flask, render_template, request



app = Flask(__name__)
#Establecer la cadena de conexion
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'posgresql://postgres:123456@localhost:5432/tareaTema3Projet'
#desactivamos la cadena de conexion
#pag 23 pps0303-Entrada de aula virtual




#pag 25 pps0303-Entrada de aula virtual
from .public import public
from .private import private

def create_app():
    app.register_blueprint(public)
    app.register_blueprint(private)
    return app