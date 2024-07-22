from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from configuration import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    db.init_app(app)

    # Import and registeration routes
    from model import User, Message  # Import to avoid circular imports
    with app.app_context():
        # Import routes here
        from application import register_routes
        register_routes(app)

    return app
