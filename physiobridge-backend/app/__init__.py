from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize SQLAlchemy
from app.models import db  # 👈 our db object from models/__init__.py

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Secret key config
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret')

    # Database config
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///physiobridge.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB with app
    db.init_app(app)

    with app.app_context():
        # Register Blueprints
        from app.views.auth_routes import auth_bp
        from app.views.booking_routes import booking_bp
        from app.views.dashboard_routes import dashboard_bp

        app.register_blueprint(auth_bp, url_prefix='/api/auth')
        app.register_blueprint(booking_bp, url_prefix='/api/bookings')
        app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')

        # Create tables
        db.create_all()

    return app
