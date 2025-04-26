from flask import Flask
from routes.mecanico_routes import Mecanico
from routes.vehiculos_routes import Vehiculo
from config.config import DATABASE_CONNECTION_URI
from models.db import db

app = Flask(__name__)


app.register_blueprint(Mecanico)


app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)



with app.app_context():
    from models.mecanico_models import Mecanico
    db.create_all()
    from models.vehiculo_models import Vehiculo
    db.create_all()


# Manejo de error 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Ruta no encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)