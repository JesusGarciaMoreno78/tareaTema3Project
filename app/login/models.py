#pag 24 pps0303-Entrada de aula virtual
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, logger


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    nombre = db.Column(db.String(20), nullable=False)
    apellidos = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


# metodo: "__str__": devuelve la concatenación de “apellidos, nombre”
    def __str__(self):
        return self.apellidos + ", " + self.nombre

# metodo: "create": almacena en base de datos el objeto
    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logger.exception(e.__str__())

# metodo: "get_by_id": recibe un id y devuelve el usuario que corresponda con ese id (método estático)
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)

# metodo: "get_by_username": recibe un username y devuelve el usuario que corresponda con ese username (método estático)
    @staticmethod
    def get_by_username(username):
        return Usuario.query.filter_by(username=username).first()


    def get_by_dni(dni):
        return Usuario.query.filter_by(dni=dni).first()

# metodo: "set_password": recibe un password y asigna al atributo password el resultado de la función hash, aplicando una salt y con método “pbkdf2:sh256:260000”
    def set_password(self, password):
        # self.password = generate_password_hash(password, method='pbkdf2:sha512')
        method = "pbkdf2:sha256:260000"
        # method = "plain"
        # method = "pbkdf2:sha512:1000000"
        self.password = generate_password_hash(password, method=method)  # Por defecto sha256
        # self.password = password.split("$", 1)[1]

# metodo: "check_password": recibe un password y devuelve un valor booleano si el password coincide con la función hash almacenada.
    def check_password(self, password):
        # passHash = 'pbkdf2:sha256:260000$' + self.password
        return check_password_hash(self.password, password)
