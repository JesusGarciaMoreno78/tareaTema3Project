from flask import render_template

from . import public

# Segundo paso Blueprint public > ultimo paso en app/_init_.py
# Este es el decorador de Blueprint que nos llevará a la raiz del modulo public
@public.route('/')
def index():  # Eta función devuelve un render_template que debemos importar
    return render_template('index.html')# render_template('index.html') lo que hace es buscar un archivo index.html y lo representa (para ello debemos importar la carpeta donde se encuentre)

