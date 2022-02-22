#pag 24 pps0303-Entrada de aula virtual
from app import db


class Cliente(db.Model):
    dni = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(), nullable=False)
# # Creamos un metodo al que le pasamos un objeto en este caso el formulario que recoge los datos a insertar en base de datos
    def nuevoCliente(self):
        db.session.add(self)
        db.session.commit()