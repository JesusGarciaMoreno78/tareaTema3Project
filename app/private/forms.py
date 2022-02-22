from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, FileField
from wtforms.validators import DataRequired, Length, ValidationError


class FiltroCliente(FlaskForm):
    dni = StringField(label="DNI", validators=[
        DataRequired("Este campo no puede estar vacío"),
        Length(message="La longitud no puede ser superior a 10 caracteres", max=10)
    ])



class NuevoCliente(FlaskForm):
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

    imagen = FileField(label="Imagen", validators=[
            FileRequired(message="El campo imagen es obligatorio"),
            FileAllowed(['jpg','png'], message="Solo jpg y png")
        ])
    #Este metodo valida imagen si fuera validate_nombre validaría la variable 'nombre'
    # def validate_imagen(form,field):
    #     max_length = 1024*1024
    #     if len(field.data.read()) > max_length:
    #         raise ValidationError(f"El fichero no puede ser superior a {max_length}")