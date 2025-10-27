# app.py
"""
Main entry point for the Flask application.
Initializes the app, loads config, and runs the server.
"""

from flask import Flask
from flask_mail import Mail
from config import SECRET_KEY, MAIL_SERVER, MAIL_PORT, MAIL_USE_SSL, MAIL_USERNAME, MAIL_PASSWORD
from routes import register_routes

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    # Email configuration
    app.config['MAIL_SERVER'] = MAIL_SERVER
    app.config['MAIL_PORT'] = MAIL_PORT
    app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
    app.config['MAIL_USERNAME'] = MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

    # Initialize Mail extension
    mail = Mail(app)

    # Register routes, passing app and mail
    register_routes(app, mail)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')