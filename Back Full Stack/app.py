from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from db import db
from config import Config

migrate = Migrate()  # Inicializamos Migrate aquí

def create_app():
    cfg = Config()
    app = Flask(__name__)

    # Configuración de la BD
    app.config["SQLALCHEMY_DATABASE_URI"] = cfg.get_database_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializar DB y Migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Importar entidades (para que Flask-Migrate las detecte)
    from entities.vehicle import Vehicle  

    # Importar y registrar controladores
    from controllers.vehicle_controller import vehicle_bp
    app.register_blueprint(vehicle_bp, url_prefix="/api")

    # Habilitar CORS
    CORS(app)

    @app.route("/")
    def home():
        return {"message": "API de Vehículos funcionando 🚀"}

    return app


if __name__ == "__main__":
    cfg = Config()
    app = create_app()
    app.run(debug=cfg.get_debug(), host="0.0.0.0", port=cfg.get_port())

