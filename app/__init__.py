# app/__init__.py
from flask import Flask

# Import the blueprint from routes.py
from app.routes import main

def create_app():
    app = Flask(__name__)
    # Configure your app if necessary, e.g., SECRET_KEY
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Register the blueprint from routes.py
    app.register_blueprint(main)

    return app