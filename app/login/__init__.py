from flask import Blueprint
# Primer paso Blueprint private > segundo paso en private/routes.py
#Instanciamos un objeto Blueprint('nombre',   'nombre de la importación(suele ser nombre del modulo por eso usamos __name__)',   'directorio plantillas',   'directorio recursos estaticos')
login = Blueprint('login', __name__, template_folder='templates', static_folder='static')

from . import routes