#pag 24 pps0303-Entrada de aula virtual
from app import db


class Cliente(db.Model):
    dni = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(20), required=True)
    apellidos = db.Column(db.String(50), required=True)
    imagen = db.Column(db.String, required=True)

