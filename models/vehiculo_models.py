from taller_.db import db  # Asegúrate de tener SQLAlchemy correctamente inicializado
from datetime import datetime

class Vehiculo(db.Model):
    __tablename__ = 'vehiculos'  # Nombre de la tabla en la base de datos

    # Atributos de la tabla Vehiculo
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    """ ID único del vehículo (clave primaria). """

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    """ ID del cliente dueño del vehículo (clave foránea hacia clientes.id). """

    marca = db.Column(db.String(100), nullable=False)
    """ Marca del vehículo, por ejemplo: Ford, Toyota. """

    modelo = db.Column(db.String(100), nullable=False)
    """ Modelo del vehículo, por ejemplo: Fiesta, Corolla. """

    año = db.Column(db.Integer, nullable=False)
    """ Año de fabricación del vehículo """

    patente = db.Column(db.String(20), unique=True, nullable=False)
    """ Patente (matrícula) del vehículo, única para cada uno. """

    # Relación inversa: permite acceder al cliente desde el vehículo
    cliente = db.relationship('Cliente', backref=db.backref('vehiculos', lazy=True))

    # Método de inicialización (Constructor)
    def __init__(self, cliente_id, marca, modelo, año, patente):
        self.cliente_id = cliente_id
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.patente = patente

    # Método de serialización (convertir a diccionario para respuestas JSON)
    def serialize(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'marca': self.marca,
            'modelo': self.modelo,
            'año': self.año,
            'patente': self.patente
        }

    def __repr__(self):
        """ Representación en texto del objeto Vehiculo """
        return f'<Vehiculo {self.marca} {self.modelo} - {self.patente}>'
        
        
