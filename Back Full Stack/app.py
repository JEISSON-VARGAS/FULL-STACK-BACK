from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

# ORM
db = SQLAlchemy()

def create_app():
    cfg = Config()
    app = Flask(__name__)

    # Configuración de la BD
    app.config["SQLALCHEMY_DATABASE_URI"] = cfg.get_database_uri()
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inicializar DB
    db.init_app(app)

    # Habilitar CORS
    CORS(app)

    # Ruta de prueba
    @app.route("/")
    def home():
        return {"message": "API de Vehículos funcionando 🚀"}

    return app

if __name__ == "__main__":
    cfg = Config()
    app = create_app()
    app.run(debug=cfg.get_debug(), port=8080)  # 👈 Forzamos el puerto 8080
