#pag 24 pps0303-Entrada de aula virtual
from flask_login import UserMixin

from app import db, logger


class Cliente(db.Model, UserMixin):
    dni = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(), nullable=False)
# # Creamos un metodo al que le pasamos un objeto en este caso el formulario que recoge los datos a insertar en base de datos
    def __str__(self):
        return self.dni

    def nuevoCliente(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logger.exception(e.__str__())