from models.db import db

class Mecanico(db.Model):
    __tablename__ = 'mecanico'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(25), nullable=False)
    apellido = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    telefono = db.Column(db.String(20), unique=True, nullable=False)
    especialidad = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, nombre, apellido, email, telefono, especialidad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.especialidad = especialidad


    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'especialidad' : self.especialidad
        }    