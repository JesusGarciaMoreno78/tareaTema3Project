# Para poder usar Flask devemos incluirlo en el archivo requerimens para poder instalarlo

from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_recaptcha import ReCaptcha
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# pag 23 pps0303-Entrada de aula virtual

app = Flask(__name__)
# en vez de clave poner una clave compleja
app.secret_key = "clave"
# Establecer la cadena de conexion
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tareaTema3Project'
# desactivamos la gestion de notificaciones de SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Instanciamos un objeto de la cxlase SQLAlchemy
app.config["RECAPTCHA_SITE_KEY"] = "6Le2QEofAAAAAISMWReQ4UQ9wCLZXB2M2Y1V-IZY"
app.config["RECAPTCHA_SECRET_KEY"] = "6Le2QEofAAAAAGvUJlO7UC8oITY9fTD1dFUWrlZm"
db = SQLAlchemy(app)
recaptcha = ReCaptcha(app)
# pag 25 pps0303-Entrada de aula virtual
# Instanciar un objeto de la classe Migrate
migrate = Migrate(app, db)
login_manager = LoginManager(app)
# Por qué si subo estos import con los de arriba no funcioana???????
from .public import public
from .private import private
from .login import login
from .admin import admin

@app.errorhandler(401)
def error_nauth(error):
    return render_template("base/error.html"),401
def create_app():
    # Úlimo paso Blueprint (registrarlo)
    app.register_blueprint(public)
    app.register_blueprint(private)
    app.register_blueprint(login)
    app.register_blueprint(admin)
    return app
