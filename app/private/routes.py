from flask import render_template, request, redirect, url_for
from setuptools.command.dist_info import dist_info
from werkzeug.datastructures import CombinedMultiDict

from . import private
from .models import Cliente
from .forms import FiltroCliente, NuevoCliente


# Segundo paso Blueprint private > ultimo paso en app/_init_.py
# Este es el decorador de Blueprint que nos llevará a private/indexcliente/
@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    formFiltro = FiltroCliente(request.form)
    if formFiltro.validate_on_submit():
        dni = formFiltro.dni.data
        cliente =  Cliente.query.filter_by(dni=dni)
        return render_template('indexcliente.html', formFiltro=formFiltro, clientes=cliente)
    else:
        clientes = Cliente.query.all()
        return render_template("indexcliente.html", clientes=clientes, formFiltro=formFiltro)

@private.route("/nuevoCliente/", methods=["GET","POST"])
def nuevoCliente():

    formnuevoCliente = NuevoCliente(CombinedMultiDict((request.files, request.form)))
    if formnuevoCliente.validate_on_submit():
        cliente = Cliente()
        cliente.dni=formnuevoCliente.dni.data
        cliente.nombre=formnuevoCliente.nombre.data
        cliente.apellidos=formnuevoCliente.apellidos.data
        cliente.imagen=formnuevoCliente.imagen.data
        #tosdos los campos
        cliente.nuevoCliente()
        return redirect(url_for('private.indexcliente'))
    return render_template("nuevoCliente.html", formnuevoCliente=formnuevoCliente)