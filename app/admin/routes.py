from flask import render_template
from flask_login import login_required, current_user
from . import admin
from ..auth.decorator import admin_required

# Segundo paso Blueprint public > ultimo paso en app/_init_.py
# Este es el decorador de Blueprint que nos llevará a la raiz del modulo public
@admin.route('/adminindex')
@login_required
@admin_required
def index():  # Eta función devuelve un render_template que debemos importar
    return render_template('administracionindex.html')# render_template('index.html') lo que hace es buscar un archivo index.html y lo representa (para ello debemos importar la carpeta donde se encuentre)

@admin.route('/adminindex/')
@login_required
@admin_required
def adminindex():
    return render_template(('adminindex.html'))