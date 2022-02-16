from flask import render_template

from . import private
#from .models import Cliente(Clase de models)



@private.route("/indexcliente/", methods=["GET","POST"])
def indexcliente():
    return render_template("indexcliente.html")
