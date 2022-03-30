from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, FileField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError


class LogUsuarioForm(FlaskForm):

    username = StringField(label="Nombre de usuario", validators=[
        DataRequired("Este campo no puede estar vacío"),
        Length(message="La longitud no puede ser superior a 15 caracteres", max=15)
    ])
    password = StringField(label="Contraseña", validators=[
        DataRequired("Este campo no puede estar vacío")
    ])

class RegistroUsuarioForm(FlaskForm):

    username = StringField(label="Nombre de usuario", validators=[
        DataRequired("Este campo no puede estar vacío"),
        Length(message="La longitud no puede ser superior a 15 caracteres", max=15)
    ])
    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])
    passwordRepeat = PasswordField(label="Repita la contraseña", validators=[
        DataRequired(message="La repetición de la contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])
    nombre = StringField(label="Nombre", validators=[
        DataRequired("Este campo no puede estar vacío"),
        Length(message="La longitud no puede ser superior a 15 caracteres", max=20)
    ])
    apellidos = StringField(label="Apellidos", validators=[
        DataRequired("Este campo no puede estar vacío"),
        Length(message="La longitud no puede ser superior a 15 caracteres", max=50)
    ])

    def validate_password(form,field):
        if str(field.data).isdigit():
            raise ValidationError("La contraseña no pueden ser solo dígitos")
        if field.data != form.passwordRepeat.data:
            raise ValidationError("No coinciden las contraseñas")

    def validate_passwordRepeat(form, field):
        if field.data != form.password.data:
            raise ValidationError("No coinciden las contraseñas")