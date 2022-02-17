from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class FiltroCliente(FlaskForm):
    dni = StringField(label="Dni", validators=[
        DataRequired("Este campo no puede estar vacío")
        Length(message="La longitud no puede ser superior a 10 caracteres", max=10)
    ]