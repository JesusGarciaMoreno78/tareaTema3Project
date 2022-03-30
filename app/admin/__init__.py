from flask import Blueprint
# Primer paso Blueprint public  > segundo paso en public/routes.py
#Instanciamos un objeto Blueprint('nombre',   'nombre de la importación(suele ser nombre del modulo por eso usamos __name__)',   'directorio plantillas',   'directorio recursos estaticos')
admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

from . import routes