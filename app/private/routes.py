from flask import render_template, request

from . import private
from .models import Cliente
from .forms import FiltroCliente
# Segundo paso Blueprint private > ultimo paso en app/_init_.py
# Este es el decorador de Blueprint que nos llevará a private/indexcliente/
@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    form = FiltroCliente(request.form)
    clientes = Cliente.query.all()
    return render_template("indexcliente.html", clientes=clientes, form=form)

