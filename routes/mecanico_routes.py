
from flask import Blueprint, jsonify, request
from models.mecanico_models import Mecanico

mecanico = Blueprint('mecanico', __name__)

@mecanico.route('/api/mecanico', methods=['GET'])
def get_mecanicos():
    try:
        
        mecanicos = Mecanico.query.all()
        
        if not mecanicos:
            return jsonify({'message': 'No se encontraron mecánicos'}), 404

        
        return jsonify([m.serialize() for m in mecanicos])

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@mecanico.route('/api/mecanico/<int:id>', methods=['GET'])
def get_mecanico_by_id(id):
    try:
        
        mecanico = Mecanico.query.get(id)

        if mecanico:
            return jsonify(mecanico.serialize())
        
        return jsonify({'message': 'Mecánico no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
