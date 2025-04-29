from flask import Blueprint, request, jsonify
from app.db import db
from app.models.vehiculo import Vehiculo

# Definimos el Blueprint
vehiculo_bp = Blueprint('vehiculo_bp', __name__)

# Ruta para obtener todos los vehículos
@vehiculo_bp.route('/vehiculos', methods=['GET'])
def get_vehiculos():
    vehiculos = Vehiculo.query.all()
    return jsonify([vehiculo.serialize() for vehiculo in vehiculos]), 200

# Ruta para obtener un vehículo por ID
@vehiculo_bp.route('/vehiculos/<int:id>', methods=['GET'])
def get_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)
    return jsonify(vehiculo.serialize()), 200

# Ruta para crear un nuevo vehículo
@vehiculo_bp.route('/vehiculos', methods=['POST'])
def create_vehiculo():
    data = request.get_json()

    nuevo_vehiculo = Vehiculo(
        cliente_id = data['cliente_id'],
        marca = data['marca'],
        modelo = data['modelo'],
        año = data['año'],
        patente = data['patente']
    )

    db.session.add(nuevo_vehiculo)
    db.session.commit()

    return jsonify(nuevo_vehiculo.serialize()), 201

# Ruta para actualizar un vehículo existente
@vehiculo_bp.route('/vehiculos/<int:id>', methods=['PUT'])
def update_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)
    data = request.get_json()

    vehiculo.cliente_id = data.get('cliente_id', vehiculo.cliente_id)
    vehiculo.marca = data.get('marca', vehiculo.marca)
    vehiculo.modelo = data.get('modelo', vehiculo.modelo)
    vehiculo.año = data.get('año', vehiculo.año)
    vehiculo.patente = data.get('patente', vehiculo.patente)

    db.session.commit()

    return jsonify(vehiculo.serialize()), 200

# Ruta para eliminar un vehículo
@vehiculo_bp.route('/vehiculos/<int:id>', methods=['DELETE'])
def delete_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)

    db.session.delete(vehiculo)
    db.session.commit()

    return jsonify({'mensaje': 'Vehículo eliminado correctamente'}), 200
