from flask import render_template, request
from setuptools.command.dist_info import dist_info

from . import private
from .models import Cliente
from .forms import FiltroCliente, GenerarCliente


# Segundo paso Blueprint private > ultimo paso en app/_init_.py
# Este es el decorador de Blueprint que nos llevará a private/indexcliente/
@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    formFiltro = FiltroCliente(request.form)
    if formFiltro.validate_on_submit():
        cliente = Cliente.query.filter_by(dni = formFiltro.dni.data)
        return render_template('indexcliente.html', formFiltro=formFiltro, cliente=cliente)
    else:
    # formGenerarCliente = GenerarCliente(request.form)
    # request
        clientes = Cliente.query.all()
        return render_template("indexcliente.html", clientes=clientes, formFiltro=formFiltro)

