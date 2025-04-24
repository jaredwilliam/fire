# Initialize the Flask app and includes configurations
from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes import main_routes

    app.register_blueprint(main_routes)

    return app
