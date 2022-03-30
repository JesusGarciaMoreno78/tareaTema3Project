import base64

from flask import render_template, request, redirect, url_for
from flask_login import current_user
from setuptools.command.dist_info import dist_info
from werkzeug.datastructures import CombinedMultiDict

from . import private
from .models import Cliente
from .forms import FiltroCliente, NuevoCliente


# Segundo paso Blueprint private > ultimo paso en app/_init_.py
# Este es el decorador de Blueprint que nos llevará a private/indexcliente/
@private.route("/indexcliente/", methods=["GET", "POST"])
def indexcliente():
    if not current_user.is_authenticated:
        return redirect(url_for("login.login"))
    formFiltro = FiltroCliente(request.form)
    if formFiltro.validate_on_submit():
        dni = formFiltro.dni.data
        cliente = Cliente.query.filter_by(dni=dni)
        return render_template('indexcliente.html', formFiltro=formFiltro, clientes=cliente)
    else:
        # Aqui habra que poner nuesro decorador decorador
        clientes = Cliente.query.all()
        return render_template("indexcliente.html", clientes=clientes, formFiltro=formFiltro)

@private.route("/nuevoCliente/", methods=["GET","POST"])
def nuevoCliente():
    if not current_user.is_authenticated:
        return redirect(url_for("login.login"))
    error=""
    formnuevoCliente = NuevoCliente(CombinedMultiDict((request.files, request.form)))
    try:
        if formnuevoCliente.validate_on_submit():
            encoded_bytes = base64.b64encode(formnuevoCliente.imagen.data.read())
            if len(encoded_bytes) > 1024*1024:
                formnuevoCliente.imagen.errors.append("Tamaño maximo 1MB")
                return render_template("nuevoCliente.html", formnuevoCliente=formnuevoCliente)
            cliente = Cliente()
            cliente.dni = formnuevoCliente.dni.data
            cliente.nombre = formnuevoCliente.nombre.data
            cliente.apellidos = formnuevoCliente.apellidos.data
            cliente.imagen = str(encoded_bytes).replace("b'", "").replace("'", "")
            cliente.nuevoCliente()
            return redirect(url_for('private.indexcliente'))
    except Exception as e:
        error=e
    return render_template("nuevoCliente.html", formnuevoCliente=formnuevoCliente,error=error)