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
from .. import app


@private.route("/indexcliente/", methods=["GET", "POST"])
def indexcliente():
    if not current_user.is_authenticated:
        return redirect(url_for("login.login"))
    formFiltro = FiltroCliente(request.form)
    if formFiltro.validate_on_submit():
        app.logger.info(f"Se busca cliente con DNI: {formFiltro.dni.data}")
        dni = formFiltro.dni.data
        cliente = Cliente.query.filter_by(dni=dni)
        if cliente:
            app.logger.info(f"Se encuentra cliente con DNI: {formFiltro.dni.data}")
        else:
            app.logger.info(f"No se encuentra cliente con DNI: {formFiltro.dni.data}")
        return render_template('indexcliente.html', formFiltro=formFiltro, clientes=cliente)
    else:
        # Aqui habra que poner nuesro decorador decorador
        app.logger.warning(f"No se pueden validar los datos del formulario")
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
                app.logger.info(f"El tamaño de la imagen del cliente {formnuevoCliente.username.data} es demasiado grande")
                formnuevoCliente.imagen.errors.append("Tamaño maximo 1MB")
                return render_template("nuevoCliente.html", formnuevoCliente=formnuevoCliente)
            cliente = Cliente()
            cliente.dni = formnuevoCliente.dni.data
            cliente.nombre = formnuevoCliente.nombre.data
            cliente.apellidos = formnuevoCliente.apellidos.data
            cliente.imagen = str(encoded_bytes).replace("b'", "").replace("'", "")
            cliente.nuevoCliente()
            app.logger.info(f"El cliente {formnuevoCliente.username.data} intenta regitrarse")
            return redirect(url_for('private.indexcliente'))
    except Exception as e:

        app.logger.warning(f"No se ha podido registrar el cliente {formnuevoCliente.username.data}")
        error=e
    return render_template("nuevoCliente.html", formnuevoCliente=formnuevoCliente,error=error)