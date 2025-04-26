from flask import Blueprint, request, jsonify
from models.vehiculo_models import Vehiculo

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
def crear_vehiculo():
    data = request.get_json()

    nuevo_vehiculo = Vehiculo(
        cliente_id = data['cliente_id'],
        marca = data['marca'],
        modelo = data['modelo'],
        año = data['año'],
        patente = data['patente']
    )

   

    return jsonify(nuevo_vehiculo.serialize()), 201

# Ruta para actualizar un vehículo existente
@vehiculo_bp.route('/vehiculos/<int:id>', methods=['PUT'])
def actualizar_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)
    data = request.get_json()

    vehiculo.cliente_id = data.get('cliente_id', vehiculo.cliente_id)
    vehiculo.marca = data.get('marca', vehiculo.marca)
    vehiculo.modelo = data.get('modelo', vehiculo.modelo)
    vehiculo.año = data.get('año', vehiculo.año)
    vehiculo.patente = data.get('patente', vehiculo.patente)

    

    return jsonify(vehiculo.serialize()), 200

# Ruta para eliminar un vehículo
@vehiculo_bp.route('/vehiculos/<int:id>', methods=['DELETE'])
def delete_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)

    

    return jsonify({'mensaje': 'Vehículo eliminado correctamente'}), 200
