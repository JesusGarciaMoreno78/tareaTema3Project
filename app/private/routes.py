from flask import render_template, request

from . import private
from .models import Cliente
from .forms import FiltroCliente

@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    form = FiltroCliente(request.form)
    clientes = Cliente.query.all()
    return render_template("indexcliente.html", clientes=clientes, form=form)

