# config.py
"""
Configuration module for the Flask app.
Handles environment variables, app config, and constants.
"""

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# App secret key
SECRET_KEY = os.getenv('APP_SECRET_KEY')

# Email configuration constants
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

# Resume download config
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CANDIDATE_NAMES = ["My_CV.pdf", "My_CV.PDF", "My_CV.docx", "My_CV", "My_CV.doc"]
DOWNLOAD_NAME = "Kehinde_Adekola_CV.pdf"  # what the user sees on download

# Email domain validation
ALLOWED_EMAIL_DOMAINS = [
    'gmail.com', 'yahoo.com', 'outlook.com', 'protonmail.com',
    'icloud.com', 'zoho.com', 'aol.com', 'yandex.com'
]

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'