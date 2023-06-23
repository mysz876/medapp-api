from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from application.config import Config
from application.init_routes import load_blueprint
from flask_cors import CORS

db = SQLAlchemy()

def create_app(config_data=Config):
    application = Flask(__name__)
    application.config.from_object(config_data)
    db.init_app(application)
    CORS(application)
    load_blueprint(application)
    return application
