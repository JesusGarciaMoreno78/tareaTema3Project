from flask import render_template, abort
from flask_login import login_required, current_user

from . import admin
from .auth.decorator import admin_required
from ..private.models import Cliente


@admin.route('/adminindex/')
@login_required
@admin_required
def adminindex():  # put application's code here
    clientes = Cliente.query.all()
    return render_template('adminindex.html', clientes=clientes)