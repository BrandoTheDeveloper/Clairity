from flask import Flask
from flask_cors import CORS
from api.routes.air_quality import bp as aq_bp
from api.config import AppConfig

def create_app() -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config.from_mapping(AppConfig().dict())
    app.register_blueprint(aq_bp, url_prefix="/api/air-quality")
    return app

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    cfg = AppConfig()
    app = create_app()
    app.run(host="0.0.0.0", port=cfg.PORT, debug=cfg.FLASK_DEBUG)
