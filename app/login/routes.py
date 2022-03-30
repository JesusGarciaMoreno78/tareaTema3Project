import base64

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from setuptools.command.dist_info import dist_info
from werkzeug.datastructures import CombinedMultiDict

import app
from . import login
from .forms import LogUsuarioForm, RegistroUsuarioForm
from .models import Usuario

PEEPER = "66a2b072-ae6a-4f49-8c3b-6668de2a2bc9"

@app.login_manager.user_loader
def load_user(user_id):
    return Usuario.get_by_id(user_id)

@login.route("/logoutsesion/")
def logout():
    logout_user()
    return redirect(url_for('public.index'))

@login.route("/nuevoUsuario/", methods=["GET","POST"])
def nuevoUsuario():
    if current_user.is_authenticated:
        return redirect(url_for("private.indexcliente"))
    error = ""
    form = RegistroUsuarioForm(request.form)
    if form.validate_on_submit():
        try:
            usuario = Usuario()
            usuario.username = form.username.data
            usuario.nombre = form.nombre.data
            usuario.apellidos = form.apellidos.data
            usuario.set_password(form.password.data + PEEPER)
            usuario.create()
            return redirect(url_for('login.login'))
        except Exception as e:
            error = "No se ha podido registrar usuario " # + e.__str__()
    return render_template("nuevoUsuario.html", form=form, error=error)

@login.route("/login/", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("private.indexcliente"))
    error = ""
    form = LogUsuarioForm(request.form)
    if form.validate_on_submit():
        try:
            username = form.username.data
            usuario = Usuario.get_by_username(username)
            try:
                if usuario and usuario.check_password(form.password.data + PEEPER):
                    login_user(usuario, False)
                    return redirect(url_for("private.indexcliente"))
                else:
                    error = "Usuario y/o contraseña incorrecta"
            except Exception as e:
                error = "no se pudo comprobar contraseña " # + e.__str__()
        except Exception as e:
            error = "No se ha podido iniciar sesión "# + e.__str__()
    return render_template("login.html", form=form, error=error)

