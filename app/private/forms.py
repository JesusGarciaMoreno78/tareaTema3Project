from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class FiltroCliente(FlaskForm):
    dni = StringField(label="DNI", validators=[
        DataRequired("Este campo no puede estar vacío"),
        Length(message="La longitud no puede ser superior a 10 caracteres", max=10)
    ])



class GenerarCliente(FlaskForm):
    ###los campos de la basede datos
    dni = StringField(label="DNI", validators=[
        DataRequired("Este campo no puede estar vacío"),
        Length(message="La longitud no puede ser superior a 10 caracteres", max=10)
    ])
    nombre = StringField(label="Nombre", validators=[
        DataRequired("Este campo no puede estar vacío"),
        Length(message="La longitud no puede ser superior a 20 caracteres", max=20)
    ])
    apellidos = StringField(label="Apellidos", validators=[
        DataRequired("Este campo no puede estar vacío"),
        Length(message="La longitud no puede ser superior a 50 caracteres", max=50)
    ])
    ## Falta la imagen

